from dreampy.redshift.netcdf import RedshiftNetCDFFile
from dreampy.utils.filterscans import FilterScans
from dreampy.redshift.plots import RedshiftPlot
import os
#import gain
import numpy as np #import required modules

sourceobs = 'J100019.7.sum'  # AzTEC5/C42 z=2.8/3.97? 
hdulist=[]
obs = 1
windows = {}
windows[0] = [(73.5,79.4)]
windows[1] = [(86.0,92.0)]
windows[2] = [(80.0,85.2)]
windows[3] = [(93.2,97.8)]
windows[4] = [(105.1,110.5)]
windows[5] = [(98.7,104.1)]
pl = RedshiftPlot()
while obs == 1:
    obslist = [36571,36572,36574,36575,36577,36578,36582,38281,38282,38284,38285,38287,38288,38295,38296,38297,38299,38300,38301,38303,38304,38305,38308,38309,38310,38312,38313,38314,38316,38317,38318,39368,39369,39370,39372,39373,39374,52764,52765]# all data
    #obslist = [36571,36572,36574,36575,36577,36578,36581,36582,36584,36585,36587,36588]# 2/18/15 Tsys=98K AzTEC5; only first 1/2 useful
    #obslist = [38281,38282,38284,38285,38287,38288,38295,38296,38297,38299,38300,38301,38303,38304,38305,38308,38309,38310,38312,38313,38314,38316,38317,38318]# 3/8/15 Tsys= 91-99K
    #obslist = [39368,39369,39370,39372,39373,39374]# 4/1/15 Tsys=89K AzTEC5
    #obslist = [52759,52760,52761,52763,52764,52765]# 12/18/15 Tsys= 101K only the last 3 ints?
    for ObsNum in obslist: #for observations in obslist
        for chassis in (0,1,2,3): #fol all chassis
            try:
                if ObsNum in (52763,52763) and chassis in (0,0):
                    continue
                if ObsNum in (35550,36392) and chassis in (2,2):
                    continue
                if ObsNum in (35550,36392) and chassis in (3,3):
                    continue
                if ObsNum > 36000:
                    fname = '/data_lmt/RedshiftChassis%s/RedshiftChassis%s_2015-02-18_0%s_00_0001.nc' % (chassis, chassis, ObsNum)          
                if ObsNum > 38200:
                    fname = '/data_lmt/RedshiftChassis%s/RedshiftChassis%s_2015-03-08_0%s_00_0001.nc' % (chassis, chassis, ObsNum)          
                if ObsNum > 39000:
                    fname = '/data_lmt/RedshiftChassis%s/RedshiftChassis%s_2015-04-01_0%s_00_0001.nc' % (chassis, chassis, ObsNum)          
                if ObsNum > 52000:
                    fname = '/data_lmt/RedshiftChassis%s/RedshiftChassis%s_2015-12-18_0%s_00_0001.nc' % (chassis, chassis, ObsNum)          
                if fname:
                    print "Process filename %s" % fname
                    nc = RedshiftNetCDFFile(fname)
                else:
                    continue
            except:
                continue
            print nc.hdu.header.SourceName
            #count += 1
            nc.hdu.process_scan()
            #el = nc.hdu.header.ElReq
            #nc.hdu.spectrum = nc.hdu.spectrum/gain.curve(el)
            ###
            # flag some chassis
          #  if ObsNum in (obslist) and chassis in(2,3): 
          #      nc.hdu.blank_frequencies( {3: [(95.,100.),]} )
            ### Flag Chassis 0
            if chassis == 0 and ObsNum in range(11000, 99350):
                nc.hdu.blank_frequencies( {2: [(85.,88.),]} )
            if chassis == 0 and ObsNum in range(50000, 60000):
                nc.hdu.blank_frequencies( {0: [(70.,99.)]} )
                nc.hdu.blank_frequencies( {1: [(70.,99.)]} )
            flaglist00=[38296,38312]    
            if chassis == 0 and ObsNum in (flaglist00):
                nc.hdu.blank_frequencies( {0: [(70.,111.),]} )
            flaglist03=[36575]    
            if chassis == 0 and ObsNum in (flaglist03):
                nc.hdu.blank_frequencies( {3: [(95.,111.),]} )
            flaglist04=[36575,36582,38301,38303]    
            if chassis == 0 and ObsNum in (flaglist04):
                nc.hdu.blank_frequencies( {4: [(95.,111.),]} )
            flaglist05=[36572,36575,36578,36582,38281,38287,38296,38297,38299,38301,38303,38308,38312,38316,38317,39369,39370,39374]    
            if chassis == 0 and ObsNum in (flaglist05):
                nc.hdu.blank_frequencies( {5: [(95.,111,),]} )
            ### Flag Chassis 1
            if chassis == 1 and ObsNum in range(31000, 39350):
                nc.hdu.blank_frequencies( {0: [(70.,100.),]} )
            if chassis == 1 and ObsNum in range(50000, 53000):
                nc.hdu.blank_frequencies( {2: [(70,100.),]} )
            flaglist10=[1000]    
            if chassis == 1 and ObsNum in (flaglist10):
                nc.hdu.blank_frequencies( {0: [(70.,111.),]} )
            flaglist13=[36575,36578,36582]    
            if chassis == 1 and ObsNum in (flaglist13):
                nc.hdu.blank_frequencies( {3: [(95.,111.),]} )
            if chassis == 1 and ObsNum in range(50000, 99500):
                nc.hdu.blank_frequencies( {3: [(97.5,100.),]} )
            flaglist14=[36574,36575,36577,36578,36582,38300]    
            if chassis == 1 and ObsNum in (flaglist14):
                nc.hdu.blank_frequencies( {4: [(95.,111.),]} )
            flaglist15=[36577,36578,36582]    
            if chassis == 1 and ObsNum in (flaglist15):
                nc.hdu.blank_frequencies( {5: [(95.,111.),]} )
            ### Flag Chassis 2
            if chassis == 2 and ObsNum in range(50000, 59500):
                nc.hdu.blank_frequencies( {2: [(75.,100.),]} )
            flaglist2=[36574,36575,36577,36578,38299,38300,38301,38303,38304,38305,38314,38316,38317,38318,39374]    
            if chassis == 2 and ObsNum in (flaglist2):
                nc.hdu.blank_frequencies( {4: [(95.,111.),]} )
                nc.hdu.blank_frequencies( {5: [(95.,111.),]} )
            flaglist20 = [38285,38288,38297,38299]
            if chassis == 2 and ObsNum in (flaglist20):
                nc.hdu.blank_frequencies( {0: [(70.,100.),]} )
            flaglist21 = [36577,36578]
            if chassis == 2 and ObsNum in (flaglist21):
                nc.hdu.blank_frequencies( {1: [(70.,100.),]} )
            flaglist22 = [1000]
            if chassis == 2 and ObsNum in (flaglist22):
                nc.hdu.blank_frequencies( {2: [(70.,100.),]} )
            flaglist23 = [1000]
            if chassis == 2 and ObsNum in (flaglist23):
                nc.hdu.blank_frequencies( {3: [(95.,100.),]} )
            if chassis == 2 and ObsNum in range(11600, 52000):
                nc.hdu.blank_frequencies( {3: [(90.,100.),]} )
            flaglist24=[38312]    
            if chassis == 2 and ObsNum in (flaglist24):
                nc.hdu.blank_frequencies( {4: [(95.,111.),]} )
            flaglist25=[36582,38308,38309]    
            if chassis == 2 and ObsNum in (flaglist25):
                nc.hdu.blank_frequencies( {5: [(95.,111.),]} )
            ### Flag Chassis 3
            flaglist3=[36575,36577,36578,36582,38300,38301,38303,38304,38305,38314,38316,38317,38318]
            if chassis == 3 and ObsNum in (flaglist3):
                nc.hdu.blank_frequencies( {4: [(95.,111.),]} )
                nc.hdu.blank_frequencies( {5: [(95.,111.),]} )
            flaglist30=[38299,39372,39374]    
            if chassis == 3 and ObsNum in (flaglist30):
                nc.hdu.blank_frequencies( {0: [(70.,100.),]} )
            flaglist32=[38312]    
            if chassis == 3 and ObsNum in (flaglist32):
                nc.hdu.blank_frequencies( {2: [(77.5,111.5),]} )
            flaglist33 = [36571,36574,36575,36577,36578,36582,38287,38288,38295,38296,38297,38299,38300,38301,38303,38304,38305,38309,38310,38312,38313,38314,38316,38317,38318,39368,39373,39374]
            if chassis == 3 and ObsNum in (flaglist33):
                nc.hdu.blank_frequencies( {3: [(95.,100.),]} )
            flaglist330 = [38308]
            if chassis == 3 and ObsNum in (flaglist330):
                nc.hdu.blank_frequencies( {3: [(90.,100.),]} )
            flaglist34=[36574]    
            if chassis == 3 and ObsNum in (flaglist34):
                nc.hdu.blank_frequencies( {4: [(95.,111.),]} )
            flaglist35=[38299,38308,38309,39368,39369,39373,52763,52764,52765]   
            if chassis == 3 and ObsNum in (flaglist35):
                nc.hdu.blank_frequencies( {5: [(95.,111,),]} )
            #
            nc.hdu.baseline(order=1, windows=windows, subtract=True)
            nc.hdu.average_all_repeats(weight='sigma')
            #
            #pl.plot_spectra(nc)
            zz = 1
            #zz = raw_input('To reject observation, type ''r'':')
            if zz != 'r':
             hdulist.append(nc.hdu)
             nc.sync()
             nc.close()
             del nc
    hdu = hdulist[0]
    hdu.average_scans(hdulist[1:],threshold_sigma=0.01)
    pl.plot_spectra(hdu)
    baselinesub = raw_input('Order of baseline (type ''n'' for none):')
    if baselinesub == 'n':
        hdu.baseline(order=0, subtract=False)
    elif baselinesub == '':
        hdu.baseline(order=0, subtract=True)
    else:
        hdu.baseline(order=int(baselinesub),subtract=True)
    txtfl = '%s.txt' % sourceobs
    hdu.make_composite_scan()
    hdu.write_composite_scan_to_ascii(txtfl)
    obs = 0
