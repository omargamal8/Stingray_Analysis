    def _make_segment_spectrum(self, lc1, lc2, segment_size):

        # TODO: need to update this for making cross spectra.
        assert isinstance(lc1, Lightcurve)
        assert isinstance(lc2, Lightcurve)

        if lc1.tseg != lc2.tseg:
            raise ValueError("Lightcurves do not have same tseg.")

        # If dt differs slightly, its propagated error must not be more than
        # 1/100th of the bin
        if not np.isclose(lc1.dt, lc2.dt, rtol=0.01 * lc1.dt/lc1.tseg):
            raise ValueError("Light curves do not have same time binning dt.")

        # In case a small difference exists, ignore it
        lc1.dt = lc2.dt

        if self.gti is None:
            self.gti = cross_two_gtis(lc1.gti, lc2.gti)

        check_gtis(self.gti)
        start_inds, end_inds = \
                bin_intervals_from_gtis(self.gti, segment_size, lc1.time,
                                    dt=lc1.dt)
    
        def _create_segments_spectrum(self, start_inds, end_inds):
                cs_all = []
                nphots1_all = []
                nphots2_all = []

                for start_ind, end_ind in zip(start_inds, end_inds):
                    time_1 = lc1.time[start_ind:end_ind]
                    counts_1 = lc1.counts[start_ind:end_ind]
                    counts_1_err = lc1.counts_err[start_ind:end_ind]
                    time_2 = lc2.time[start_ind:end_ind]
                    counts_2 = lc2.counts[start_ind:end_ind]
                    counts_2_err = lc2.counts_err[start_ind:end_ind]
                    lc1_seg = Lightcurve(time_1, counts_1, err=counts_1_err,
                                         err_dist=lc1.err_dist,
                                         gti=[[time_1[0] - lc1.dt/2,
                                               time_1[-1] + lc1.dt / 2]],
                                         dt=lc1.dt)
                    lc2_seg = Lightcurve(time_2, counts_2, err=counts_2_err,
                                         err_dist=lc2.err_dist,
                                         gti=[[time_2[0] - lc2.dt/2,
                                               time_2[-1] + lc2.dt / 2]],
                                         dt=lc2.dt)
                    cs_seg = Crossspectrum(lc1_seg, lc2_seg, norm=self.norm)
                    cs_all.append(cs_seg)
                    nphots1_all.append(np.sum(lc1_seg.counts))
                    nphots2_all.append(np.sum(lc2_seg.counts))
                return cs_all, nphots1_all, nphots2_all

        from multiprocessing import cpu_count
        from dask import compute, delayed
        import dask.multiprocessing

        processes_count = cpu_count()
        tasks = []
        for i in range(processes):
            process_share = int( len(start_inds) / processes_count )
            starting_index = i * process_share
            ending_index = (starting_index + process_share) % len(start_inds)
            tasks.append(delayed(_create_segments_spectrum)(start_inds[starting_index:ending_index], end_inds[starting_index:ending_index]))
        cs_all = []
        nphotos1_all = []
        nphotos2_all = []

        results = compute(*tasks, get = dask.multiprocessing.get)
        for cs, nphoto1, nphoto2 in list(results):
            cs_all.append(cs)
            nphotos1_all.append(nphoto1)
            nphotos2_all.append(nphotos2)
        
    