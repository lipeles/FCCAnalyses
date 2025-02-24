import ROOT
from examples.FCChh.vbf_hww.analysis_final import histoList,cutList
import examples.FCChh.vbf_hww.analysis_config as analysis_config

# global parameters
intLumi        = 30e+06 #in pb-1
ana_tex        = 'VBF H#rightarrow WW #rightarrow llvv'
delphesVersion = '3.4.2'
energy         = 100
collider       = 'FCC-hh'
inputDir       = analysis_config.final_output
formats        = ['png',] #'pdf']
yaxis          = ['log',] #'log']
stacksig       = ['nostack']
# stacksig       = ['stack','nostack']
outdir         = analysis_config.plots_output
plotStatUnc    = True

#variables = ['n_el','n_mu','n_lep']
variables = histoList.keys()

# rebin = [1, 1, 1, 1, 2] # uniform rebin per variable (optional)

### Dictionary with the analysis name as a key, and the list of selections to be plotted for this analysis. The name of the selections should be the same than in the final selection

extralabel = {}
# extralabel['sel0_all'] = "Preselection Events"
# extralabel['sel1_bjeteveto'] = "b-jet veto"
# extralabel['sel2_jeteveto'] = "2-jet exclusive"
# extralabel['sel3_both'] = "2-jet exclusive and b-jet veto"
# extralabel['sel4_mtautau'] = "Z#rightarrow#tau#tau veto"
# extralabel['sel5_mjj'] = "mjj cut applied"
# extralabel['sel6_mem'] = "m_em cut applied"
# extralabel['sel7_mjj_dphiem_lepcent'] = "m_{jj}, #Delta#eta_{jj}, #Delta#phi_{em}, lep cent"
# extralabel['sel8_mjj_dphiem_lepcent_mt'] = extralabel['sel7_mjj_dphiem_lepcent'] + ", MT"
extralabel = cutList

selections = {}
selections['vbf_hww']   = extralabel.keys()


colors = {}
colors['vbf_hww'] = ROOT.kRed
colors['vbf_ww'] = ROOT.kOrange
colors['ggH'] = ROOT.kTeal
colors['ttbar'] = ROOT.kBlue
colors['z_tautau'] = ROOT.kViolet
colors['vbf_z_tautau'] = ROOT.kViolet-20
colors['vv_lep'] = ROOT.kGreen



# this is selection: signal/backgrounds category : {final histo label : [set of input procs]}
plots = {}
plots['vbf_hww']={}
plots['vbf_hww']['signal']={}
plots['vbf_hww']['backgrounds']={}

procs = {}
procs['vbf_hww_llvv'] = ['signal','vbf_hww']
procs['mgp8_pp_vbf_ww_lvlv_5f_noHiggs_100TeV'] = ['signal','vbf_ww']
procs['mgp8_pp_vbf_h01j_5f_hwwlvlv'] = ['signal','vbf_hww']
procs['ggh_hww_llvv'] = ['backgrounds','ggH']
procs['ttbar_lep'] = ['backgrounds','ttbar']
procs['mgp8_pp_tt012j_5f_blvblv'] = ['backgrounds','ttbar']
procs['z_tautau'] = ['backgrounds','z_tautau']
procs['vv_lep'] = ['backgrounds','vv_lep']
procs['mgp8_pp_z0123j_4f_ztautau'] = ['backgrounds','z_tautau']


for proc in analysis_config.process_list:
    proc_config = procs[proc]
    if not proc in plots['vbf_hww'][proc_config[0]]:
        plots['vbf_hww'][proc_config[0]][proc_config[1]]=[]
    plots['vbf_hww'][proc_config[0]][proc_config[1]].append(proc)

print(plots)

legend = {}
legend['vbf_hww'] = 'VBF H #rightarrow WW'
legend['vbf_ww'] = 'VBF  WW (no Higgs)'
legend['ggH'] = 'gg #rightarrow H #rightarrow WW'
legend['ttbar'] = 't#bar{t}'
legend['z_tautau'] = 'Z #rightarrow #tau#tau'
legend['vbf_z_tautau'] = 'VBF Z #rightarrow #tau#tau'
legend['vv_lep'] = 'VV leptonic'
