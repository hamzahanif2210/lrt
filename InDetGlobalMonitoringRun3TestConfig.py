#
#  Copyright (C) 2002-2020 CERN for the benefit of the ATLAS collaboration
#



####################################################
#                                                  #
# InDetGlobalManager top algorithm                 #
#                                                  #
####################################################

def InDetGlobalMonitoringRun3TestConfig(flags):
    from AthenaConfiguration.ComponentAccumulator import ComponentAccumulator
    acc = ComponentAccumulator()
    
    from AthenaMonitoring import AthMonitorCfgHelper
    helper = AthMonitorCfgHelper(flags, "InDetGlobalMonitoringRun3Test")
        
    from AthenaConfiguration.ComponentFactory import CompFactory

    # run on RAW only
    if flags.DQ.Environment in ('online', 'tier0', 'tier0Raw'):
        ##        from InDetRecExample.InDetKeys import InDetKeys    ## not sure it works now
        
        ########### here begins InDetGlobalTrackMonAlg ###########
        kwargsInDetGlobalTrackMonAlg = { 
            'DoIBL' : True,                       #InDetFlags.doIBL(), #Turn on/off IBL histograms 
            'TrackName'  : 'CombinedInDetTracks',  #Until new config ready
            'TrackName2' : 'CombinedInDetTracks',  #Until new config ready
            'TrackName3' : 'CombinedInDetTracks',  #Until new config ready
        }
        
        
        from InDetGlobalMonitoringRun3Test.InDetGlobalTrackMonAlgCfg import InDetGlobalTrackMonAlgCfg 

        inDetGlobalTrackMonAlg = helper.addAlgorithm(CompFactory.InDetGlobalTrackMonAlg, 'InDetGlobalTrackMonAlg')
        for k, v in kwargsInDetGlobalTrackMonAlg.items():
            setattr(inDetGlobalTrackMonAlg, k, v)

        inDetGlobalTrackMonAlg.TrackSelectionTool = CompFactory.InDet.InDetTrackSelectionTool('InDetGlobalTrackMonAlg_TrackSelectionTool')
        inDetGlobalTrackMonAlg.TrackSelectionTool.UseTrkTrackTools = True
        inDetGlobalTrackMonAlg.TrackSelectionTool.CutLevel         = "TightPrimary"
        inDetGlobalTrackMonAlg.TrackSelectionTool.maxNPixelHoles   = 1
        inDetGlobalTrackMonAlg.TrackSelectionTool.minPt            = 5000
        #        InDetGlobalTrackMonAlg.Baseline_TrackSelectionTool.TrackSummaryTool = InDetTrackSummaryTool
        #        InDetGlobalTrackMonAlg.Baseline_TrackSelectionTool.Extrapolator     = InDetExtrapolator
        #
        inDetGlobalTrackMonAlg.Tight_TrackSelectionTool = CompFactory.InDet.InDetTrackSelectionTool('InDetGlobalTrackMonAlg_TightTrackSelectionTool')
        inDetGlobalTrackMonAlg.Tight_TrackSelectionTool.UseTrkTrackTools = True
        inDetGlobalTrackMonAlg.Tight_TrackSelectionTool.CutLevel         = "TightPrimary"
        inDetGlobalTrackMonAlg.Tight_TrackSelectionTool.minPt            = 5000
        #        InDetGlobalTrackMonAlg.Tight_TrackSelectionTool.TrackSummaryTool = InDetTrackSummaryTool
        #        InDetGlobalTrackMonAlg.Tight_TrackSelectionTool.Extrapolator     = InDetExtrapolator
        

        # Run 3 configs - stolen from SCT
        from SCT_Monitoring.TrackSummaryToolWorkaround import TrackSummaryToolWorkaround
        InDetTrackSummaryTool = acc.popToolsAndMerge(TrackSummaryToolWorkaround(flags))
        inDetGlobalTrackMonAlg.TrackSummaryTool = InDetTrackSummaryTool
        inDetGlobalTrackMonAlg.TrackSelectionTool.TrackSummaryTool = InDetTrackSummaryTool
        inDetGlobalTrackMonAlg.TrackSelectionTool.Extrapolator     = acc.getPublicTool("InDetExtrapolator")
        inDetGlobalTrackMonAlg.Tight_TrackSelectionTool.TrackSummaryTool = InDetTrackSummaryTool
        inDetGlobalTrackMonAlg.Tight_TrackSelectionTool.Extrapolator     = acc.getPublicTool("InDetExtrapolator")
        
        InDetGlobalTrackMonAlgCfg(helper, inDetGlobalTrackMonAlg, **kwargsInDetGlobalTrackMonAlg)
        ########### here ends InDetGlobalTrackMonAlg ###########

        ########### here begins InDetGlobalLRTMonAlg ###########
        kwargsInDetGlobalLRTMonAlg = { 
            'DoIBL' : True,                       #InDetFlags.doIBL(), #Turn on/off IBL histograms 
            'LRTName'  : 'CombinedInDetLRTs',  #Until new config ready
            'LRTName2' : 'CombinedInDetLRTs',  #Until new config ready
            'LRTName3' : 'CombinedInDetLRTs',  #Until new config ready
        }
        
        
        from InDetGlobalMonitoringRun3Test.InDetGlobalLRTMonAlgCfg import InDetGlobalLRTMonAlgCfg 

        inDetGlobalLRTMonAlg = helper.addAlgorithm(CompFactory.InDetGlobalLRTMonAlg, 'InDetGlobalLRTMonAlg')
        for k, v in kwargsInDetGlobalLRTMonAlg.items():
            setattr(inDetGlobalLRTMonAlg, k, v)

        inDetGlobalLRTMonAlg.LRTSelectionTool = CompFactory.InDet.InDetLRTSelectionTool('InDetGlobalLRTMonAlg_LRTSelectionTool')
        inDetGlobalLRTMonAlg.LRTSelectionTool.UseTrkLRTTools = True
        inDetGlobalLRTMonAlg.LRTSelectionTool.CutLevel         = "TightPrimary"
        inDetGlobalLRTMonAlg.LRTSelectionTool.maxNPixelHoles   = 1
        inDetGlobalLRTMonAlg.LRTSelectionTool.minPt            = 5000
        #        InDetGlobalLRTMonAlg.Baseline_LRTSelectionTool.LRTSummaryTool = InDetLRTSummaryTool
        #        InDetGlobalLRTMonAlg.Baseline_LRTSelectionTool.Extrapolator     = InDetExtrapolator
        #
        inDetGlobalLRTMonAlg.Tight_LRTSelectionTool = CompFactory.InDet.InDetLRTSelectionTool('InDetGlobalLRTMonAlg_TightLRTSelectionTool')
        inDetGlobalLRTMonAlg.Tight_LRTSelectionTool.UseTrkLRTTools = True
        inDetGlobalLRTMonAlg.Tight_LRTSelectionTool.CutLevel         = "TightPrimary"
        inDetGlobalLRTMonAlg.Tight_LRTSelectionTool.minPt            = 5000
        #        InDetGlobalLRTMonAlg.Tight_LRTSelectionTool.LRTSummaryTool = InDetLRTSummaryTool
        #        InDetGlobalLRTMonAlg.Tight_LRTSelectionTool.Extrapolator     = InDetExtrapolator
        

        # Run 3 configs - stolen from SCT
        from SCT_Monitoring.LRTSummaryToolWorkaround import LRTSummaryToolWorkaround
        InDetLRTSummaryTool = acc.popToolsAndMerge(LRTSummaryToolWorkaround(flags))
        inDetGlobalLRTMonAlg.LRTSummaryTool = InDetLRTSummaryTool
        inDetGlobalLRTMonAlg.LRTSelectionTool.LRTSummaryTool = InDetLRTSummaryTool
        inDetGlobalLRTMonAlg.LRTSelectionTool.Extrapolator     = acc.getPublicTool("InDetExtrapolator")
        inDetGlobalLRTMonAlg.Tight_LRTSelectionTool.LRTSummaryTool = InDetLRTSummaryTool
        inDetGlobalLRTMonAlg.Tight_LRTSelectionTool.Extrapolator     = acc.getPublicTool("InDetExtrapolator")
        
        InDetGlobalLRTMonAlgCfg(helper, inDetGlobalLRTMonAlg, **kwargsInDetGlobalLRTMonAlg)
        ########### here ends InDetGlobalLRTMonAlg ###########

        
    # run on ESD
    if flags.DQ.Environment != 'tier0Raw':
        ########### here begins InDetGlobalPrimaryVertexMonAlg ###########
        from InDetGlobalMonitoringRun3Test.InDetGlobalPrimaryVertexMonAlgCfg import InDetGlobalPrimaryVertexMonAlgCfg 
        
        myInDetGlobalPrimaryVertexMonAlg = helper.addAlgorithm(CompFactory.InDetGlobalPrimaryVertexMonAlg,
                                                               'InDetGlobalPrimaryVertexMonAlg')
        
        kwargsInDetGlobalPrimaryVertexMonAlg = { 
            'vxContainerName'                      : 'PrimaryVertices', #InDetKeys.xAODVertexContainer(),
            'vxContainerNameWithOutBeamConstraint' : 'VxPrimaryCandidateWithBeamConstraint', #InDetKeys.PrimaryVerticesWithoutBeamConstraint(),
            'vxContainerNameSplit'                 : 'VxPrimaryCandidateSplitStream', #InDetKeys.PrimaryVerticesSplitStream(),
            'doEnhancedMonitoring'                 : True # InDetFlags.doMonitoringPrimaryVertexingEnhanced()
        }
        
        for k, v in kwargsInDetGlobalPrimaryVertexMonAlg.items():
            setattr(myInDetGlobalPrimaryVertexMonAlg, k, v)
            
        InDetGlobalPrimaryVertexMonAlgCfg(helper, myInDetGlobalPrimaryVertexMonAlg, **kwargsInDetGlobalPrimaryVertexMonAlg)

        ########### here ends InDetGlobalPrimaryVertexMonAlg ###########

        ########### here begins InDetGlobalBeamSpotMonAlg ###########
        from BeamSpotConditions.BeamSpotConditionsConfig import BeamSpotCondAlgCfg
        acc.merge(BeamSpotCondAlgCfg(flags))
       
        from InDetGlobalMonitoringRun3Test.InDetGlobalBeamSpotMonAlgCfg import InDetGlobalBeamSpotMonAlgCfg 
        
        myInDetGlobalBeamSpotMonAlg = helper.addAlgorithm(CompFactory.InDetGlobalBeamSpotMonAlg,
                                                          'InDetGlobalBeamSpotMonAlg')
        
        kwargsInDetGlobalBeamSpotMonAlg = { 
            'BeamSpotKey'                      : 'BeamSpotData', #InDetKeys.BeamSpotData(),
            'vxContainerName'                  : 'PrimaryVertices', #InDetKeys.xAODVertexContainer(),
            'trackContainerName'               : 'InDetTrackParticles', #InDetKeys.xAODTrackParticleContainer(),
            'useBeamspot'                      : True, # InDetFlags.useBeamConstraint()
            'vxContainerWithBeamConstraint'    : False # InDetFlags.useBeamConstraint()
        }
        
        for k, v in kwargsInDetGlobalBeamSpotMonAlg.items():
            setattr(myInDetGlobalBeamSpotMonAlg, k, v)

        InDetGlobalBeamSpotMonAlgCfg(helper, myInDetGlobalBeamSpotMonAlg, **kwargsInDetGlobalBeamSpotMonAlg)

        ########### here ends InDetGlobalBeamSpotMonAlg ###########
        
    acc.merge(helper.result())
    return acc
