import os.path

from lsst.utils import getPackageDir

cfhtConfigDir = os.path.join(getPackageDir("obs_cfht"), "config")
config.calibrate.photocal.colorterms.load(os.path.join(cfhtConfigDir, 'colorterms.py'))

from lsst.obs.cfht.cfhtIsrTask import CfhtIsrTask
config.isr.retarget(CfhtIsrTask)

config.isr.doBias = False
config.isr.doDark = False
config.isr.doFlat = False
config.isr.doFringe = False
config.isr.fringeAfterFlat = False
config.isr.doWrite = False
config.isr.setGainAssembledCcd = True
config.isr.assembleCcd.doRenorm = False
config.isr.assembleCcd.setGain = False
config.isr.fringe.filters = ['i', 'i2', 'z']
config.isr.fringe.pedestal = True
config.isr.fringe.small = 1
config.isr.fringe.large = 50
config.isr.doAssembleIsrExposures = True

config.calibrate.repair.doCosmicRay=True
config.calibrate.repair.cosmicray.cond3_fac=2.5
config.calibrate.repair.cosmicray.cond3_fac2=0.4
config.calibrate.repair.cosmicray.niteration=3
config.calibrate.repair.cosmicray.nCrPixelMax=100000
config.calibrate.repair.cosmicray.minSigma=6.0
config.calibrate.repair.cosmicray.min_DN=150.0

config.calibrate.initialPsf.fwhm=1.0

config.calibrate.measurePsf.starSelector.name = "objectSize"

try :
    # AstrometryTask, the default
    config.calibrate.astrometry.refObjLoader.filterMap = {
        'i2': 'i',
    }
    config.calibrate.astrometry.wcsFitter.order = 3
    config.calibrate.astrometry.matcher.maxMatchDistArcSec=5
except :
    # ANetAstrometryTask
    config.calibrate.astrometry.solver.filterMap = {
        'i2': 'i',
    }

config.calibrate.photocal.applyColorTerms = True
config.calibrate.photocal.photoCatName="e2v"
