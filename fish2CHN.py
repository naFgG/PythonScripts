import pandas as pd
import os
from glob import glob

species = {'Gambusia_affinis': '食蚊鱼', 'Tachysurus_fulvidraco': '黄颡鱼', 'Anabarilius_brevianalis': '短臀白鱼',
           'Parmaturus_melanobranchus': '黑鳃双锯鲨', 'Gambusia_holbrooki': '东部食蚊鱼', 'Tridentiger_barbatus': '髭缟虾虎鱼',
           'Ctenopharyngodon_idella': '草鱼', 'Salarias_fasciatus': '细纹凤鳚', 'Boleophthalmus_pectinirostris': '大弹涂鱼',
           'Pterapogon_kauderni': '考氏鳍竺鲷', 'Channa_argus': '乌鳢', 'Takifugu_rubripes': '红鳍东方鲀',
           'Pampus_chinensis': '中国鲳', 'Parabramis_pekinensis': '鳊', 'Eleutheronema_tetradactylum': '四指马鲅',
           'Tachysurus_intermedius': '亨氏拟鲿', 'Channa_maculata': '斑鳢',
           'Megalobrama_terminalis_x_Megalobrama_amblycephala': '三角鲂_x_团头鲂', 'Pellona_flavipinnis': '黄鳍多齿鳓',
           'Danio_rerio': '斑马鱼', 'Coilia_brachygnathus': '短颌鲚', 'Muraenesox_cinereus': '海鳗',
           'Ctenopharyngodon_idellus_x_Elopichthys_bambusa': '草鱼_x_鳡', 'Chitala_chitala': '铠甲弓背鱼',
           'Gadus_morhua': '大西洋鳕', 'Osteoglossum_bicirrhosum': '双须骨舌鱼',
           'Cyprinus_carpio_x_Megalobrama_amblycephala': '鲤鱼_x_团头鲂', 'Micropercops_swinhonis': '小黄黝鱼',
           'Rhinogobius_duospilus': '溪吻虾虎鱼', 'Cyprinus_carpio_haematopterus': '锦鲤', 'Sarotherodon_lohbergeri': '洛氏帚齿非鲫',
           'Rhinogobius_wuyanlingensis': '乌岩岭吻虾虎鱼', 'Heterodontus_francisci': '佛氏虎鲨', 'Tetraodon_fluviatilis': '东方鲀',
           'Plagiognathops_microlepis': '细鳞斜颌鲴', 'Melanogrammus_aeglefinus': '黑线鳕', 'Rhinogobius_cliffordpopei': '波氏吻虾虎鱼',
           'Cyprinus_carpio_haematopterus_x_Megalobrama_amblycephala': '锦鲤_x_团头鲂', 'Anabarilius_grahami': '白鱼',
           'Cyprinus_carpio_\'Guilin\'': '镜鲤', 'Oreochromis_mossambicus': '罗非鱼', 'Polyodon_spathula': '匙吻鲟',
           'Eupleurogrammus_muticus': '小带鱼', 'Tridentiger_bifasciatus': '双带缟虾虎鱼', 'Takifugu_xanthopterus': '黄鳍东方鲀',
           'Stolephorus_insularis': '岛屿小公鱼', 'Stomatepia_pindu': '平德大口非鲫',
           'Takifugu_flavidus_x_Takifugu_rubripes': '菊黄东方鲀_x_红鳍东方鲀', 'Channa_striata': '线鳢',
           'Chanodichthys_dabryi': '达氏鲌', 'Phoxinus_oxycephalus': '尖头鱥',
           'Megalobrama_amblycephala_x_Elopichthys_bambusa': '团头鲂_x_鳡', 'Coilia_mystus': '凤鲚',
           'Tetraodon_nigroviridis': '绿河鲀', 'Cynoglossus_joyneri': '短吻红舌鳎', 'Coilia_grayii': '七丝鲚',
           'Harpadon_nehereus': '龙头鱼', 'Tachysurus_vachellii': '瓦氏黄颡鱼', 'Channa_marulius': '眼鳢',
           'Tridentiger_brevispinis': '短棘缟虾虎鱼', 'Setipinna_taty': '黄鲫', 'Pimephales_notatus': '钝吻胖头鱥',
           'Pseudolaubuca_engraulis': '寡鳞飘鱼', 'Arothron_stellatus': '星斑叉鼻鲀', 'Microspathodon_chrysurus': '金色小叶齿鲷',
           'Tatia_intermedia': '中间特鲶', 'Rhina_ancylostoma': '圆犁头鳐', 'Leiocassis_longirostris': '长吻鮠',
           'Hemiculterella_macrolepis': '大鳞半䱗', 'Carassius_carassius': '黑鲫', 'Gadus_macrocephalus': '大头鳕',
           'Xenocypris_fangi': '方氏鲴', 'Trypauchen_vagina': '孔虾虎鱼', 'Merlangius_merlangus': '牙鳕',
           'Distoechodon_tumirostris': '圆吻鲴', 'Bostrychus_sinensis': '中华乌塘鳢', 'Stegastes_fasciolatus': '蓝纹高身雀鲷',
           'Ctenotrypauchen_chinensis': '中华栉孔虾虎鱼',
           'Oreochromis_niloticus_x_Oreochromis_mossambicus': '尼罗罗非鱼_x_罗非鱼', 'Acanthurus_xanthopterus': '黄翼刺尾鱼',
           'Macrhybopsis_aestivalis': '夏鮈鱥', 'Muraenolepis_microps': '小眼鳗鳞鳕', 'Reinhardtius_hippoglossoides': '马舌鲽',
           'Dissostichus_eleginoides': '小鳞犬牙南极鱼', 'Pampus_sp._Li_et_al., 2014': '鲳_sp._Li_et_al., 2014',
           'Hemiculter_leucisculus': '䱗', 'Ancherythroculter_nigrocauda': '黑尾近红鲌', 'Takifugu_oblongus': '横纹东方鲀',
           'Gadus_chalcogrammus': '黄线狭鳕', 'Chiloscyllium_sp._SH': '斑竹鲨属_sp._SH', 'Procypris_mera': '乌原鲤',
           'Takifugu_alboplumbeus': '铅点东方鲀', 'Sinocyclocheilus_ronganensis': '融安金线鲃', 'Oreochromis_niloticus': '尼罗罗非鱼',
           'Carassius_auratus_auratus': '鲫', 'Carassius_auratus_x_Cyprinus_carpio_x_Carassius_cuvieri': '金鱼_x_鲤_x_日本鲫',
           'Cyprinus_carpio': '鲤', 'Oreochromis_esculentus': '美味口孵非鲫', 'Notropis_texanus': '杂色美洲鱥',
           'Tridentiger_kuroiwae': '黃斑缟虾虎魚', 'Rhinogobius_sp._HYW-2001': '吻虾虎鱼sp._HYW-2001', 'Rhodeus_uyekii': '朝鲜鳑鲏',
           'Rhodeus_ocellatus': '高体鳑鲏', 'Eleotris_oxycephala': '尖头塘鳢', 'Sinobdella_sinensis': '中华刺鳅',
           'Pseudorasbora_parva': '麦穗鱼', 'Macrognathus_aculeatus': '长吻棘鳅', 'Odontobutis_potamophila': '河川沙塘鳢',
           'Sebastes_melanostictus': '黑斑平鲉', 'Lepidocybium_flavobrunneum': '异鳞蛇鲭', 'Rhinogobius_similis': '真吻虾虎鱼',
           'Anarhichas_denticulatus': '小齿狼鱼', 'Sebastes_mentella': '尖吻平鲉', 'Antimora_rostrata': '蓝拟深海鳕',
           'Halargyreus_johnsonii': '约氏双臀深海鳕', 'Sebastes_norvegicus': '金平鲉', 'Microgadus_proximus': '太平洋小鳕',
           'Eleginus_gracilis': '远东宽突鳕', 'Microgadus_tomcod': '大西洋小鳕', 'Ariosoma_major': '大锥体康吉鳗',
           'Rhinochimaera_africana': '非洲长鼻银鲛', 'Lepomis_auritus': '绿太阳鱼', 'Fundulopanchax_sjostedti': '蓝旗鮰',
           'Harttiella_lucifer': 'Harttiella_lucifer(无中文名)', 'Schistura_sikmaiensis': '锡克曼南鳅',
           'Hemilepidotus_spinosus': '褐杂鳞杜父鱼', 'Zebrasoma_rostratum': '长嘴倒鲷', 'Akarotaxis_nudiceps': '裸头龙鰧',
           'Channa_bankanensis': '斑卡鳢', 'Scomberomorus_munroi_x_Scomberomorus_semifasciatus': '澳洲马鲛_x_横纹鲅鱼',
           'Pseudomystus_leiacanthus': '光刺鮠', 'Prionodraco_evansii': '锯渊龙鰧', 'Maurolicus_weitzmani': '韦茨穆氏暗光鱼',
           'Chimaera_monstrosa': '大西洋银鲛', 'Percina_brevicauda': '短尾小鲈', 'Aesopia_cornuta': '角鳎',
           'Brachysomophis_crocodilinus': '鳄形短体蛇鳗', 'Pagrus_auratus': '金赤鲷', 'Pempheris_schomburgkii': '斯氏单鳍鱼',
           'Ariosoma_shiroanago': '大锥体糯鳗', 'Nibea_coibor': '浅色黄姑鱼', 'Acentronura_tentaculata': '南非细尾海马',
           'Misgurnus_anguillicaudatus_x_Misgurnus_bipartitus': '泥鳅_x_北方泥鳅', 'Pseudobrama_simoni': '似鳊',
           'Misgurnus_anguillicaudatus': '泥鳅', 'Rhinogobius_brunneus': '褐吻虾虎鱼', 'Rhinogobius_nagoyae': '名古屋吻虾虎鱼',
           'Pristipomoides_typus': '紫鱼', 'Carassioides_acuminatus': '须鲫', 'Luciocyprinus_langsoni': '似鳡',
           'Sinocyclocheilus_oxycephalus': '尖头金线鲃', 'Sinocyclocheilus_anophthalmus': '无眼金线鲃',
           'Paralaubuca_barroni': '罗碧鱼', 'Discocheilus_wui': '伍氏盘口鲮', 'Rhynchocypris_lagowskii': '拉氏鱥',
           'Tanakia_himantegus_chii': '革条田中鳑鲏', 'Gobiomorphus_australis': '澳洲鮈塘鳢', 'Oxyeleotris_lineolata': '线纹尖塘鳢',
           'Gobiomorphus_breviceps': '短头鮈塘鳢', 'Hypsoblennius_gentilis': '海湾高䲁', 'Acrossocheilus_yunnanensis': '云南光唇鱼',
           'Scaphiodonichthys_acanthopterus': '刺鳍铲齿鱼', 'Cheilodactylus_fasciatus': '条纹唇指䱵',
           'Sander_lucioperca': '梭鲈', 'Moolgarda_cunnesius': '长鳍莫鲻', 'Acrossocheilus_kreyenbergii': '薄颌光唇鱼',
           'Rhinogobius_yonezawai': 'Rhinogobius_yonezawai(无中文名)', 'Carassius_gibelio': '银鲫',
           'Chanodichthys_recurviceps': '海南鲌', 'Sinocyclocheilus_yishanensis': '宜山金线鲃',
           'Rhinogobius_flumineus': '河川吻虾虎', 'Paramisgurnus_dabryanus': '大鳞副泥鳅',
           'Tridentiger_trigonocephalus': '纹缟虾虎鱼', 'Acheilognathus_macropterus': '大鳍鱊', 'Culter_alburnus': '翘嘴鲌',
           'Abbottina_rivularis': '棒花鱼', 'Lagocephalus_spadiceus': '棕斑兔头鲀', 'Acheilognathus_barbatus': '须鱊',
           'Sineleotris_chalmersi': '海南华黝鱼', 'Grammistes_sexlineatus': '六带线纹鱼',
           'Cynoglossus_lighti': '长吻红舌鳎', 'Chanodichthys_erythropterus': '红鳍原鲌', 'Abbottina_obtusirostris': '钝吻棒花鱼',
           'Hypophthalmichthys_nobilis': '鳙', 'Siganus_canaliculatus': '长鳍篮子鱼',
           'Hypophthalmichthys_nobilis_x_Hypophthalmichthys_molitrix': '鳙_x_鲢', 'Sphaeramia_orbicularis': '环纹圆天竺鲷',
           'Microdous_chalmersi': '海南细齿塘鳢', 'Chaeturichthys_stigmatias': '矛尾虾虎鱼', 'Jaydia_lineata': '细条天竺鲷',
           'Rhodeus_ocellatus_ocellatus': '高体鳑鲏', 'Valenciennea_puellaris': '范氏虾虎鱼', 'Rhodeus_fangi': '方氏鳑鲏',
           'Alosa_sapidissima': '美洲鲥', 'Tenualosa_reevesii': '鲥', 'Odontamblyopus_lacepedii': '红狼牙虾虎鱼',
           'Sardinella_melanura': '黑尾小沙丁鱼', 'Strophidon_sathete': '钱鳗', 'Clidoderma_asperrimum': '粒鲽',
           'Rhinogobius_davidi': '戴氏吻虾虎鱼', 'Chiloscyllium_plagiosum': '条纹斑竹鲨', 'Clinostomus_elongatus': '斜口鱥鱼',
           'Notropis_bifrenatus': '双缰美洲鱥', 'Cirrhinus_reba': '南亚鲮', 'Crossocheilus_siamensis': '暹罗角鱼',
           'Cophecheilus_bamen': 'Cophecheilus_bamen(无中文名)', 'Glossamia_aprion': '舌天竺鲷', 'Abbottina_binhi': '越南棒花鱼',
           'Labiobarbus_leptocheilus': '细唇长背魮', 'Tampichthys_erimyzonops': '墨西哥坦鱥', 'Phoxinus_bigerri': '贝氏莫罗鱥',
           'Parachela_siamensis': '暹罗副元宝鯿', 'Labeo_bata': '巴塔野鲮', 'Zacco_platypus': '宽鳍鱲',
           'Tariqlabeo_bicornis': '角鱼', 'Apogon_hyalosoma': '扁头天竺鲷', 'Eremichthys_acros': '内华达漠鱼',
           'Peristedion_nierstraszi': '带黄鲂鮄', 'Phoxinus_oxycephalus_jouyi': '焦氏尖頭鱥', 'Megalobrama_terminalis': '三角鲂',
           'Hybopsis_winchelli': '温氏鮈鱥', 'Hippoglossus_stenolepis': '狭鳞庸鲽', 'Huso_dauricus': '达氏鳇',
           'Acipenser_brevirostrum': '短吻鲟', 'Trichiurus_japonicus': '带鱼', 'Carcharhinus_leucas': '公牛真鲨',
           'Acanthogobius_luridus': '棕刺虾虎鱼', 'Tenualosa_ilisha': '云鲥', 'Scoliodon_laticaudus': '尖头斜齿鲨',
           'Maculabatis_pastinacoides': 'Maculabatis_pastinacoides(无中文名)', 'Collichthys_niveatus': '黑鳃梅童鱼',
           'Plagioscion_sp._BLS-2003': '异鳞石首鱼属sp._BLS-2003', 'Taenioides_sp._HYS-2014': '鳗虾虎鱼属sp._HYS-2014',
           'Miichthys_miiuy': '鮸', 'Collichthys_lucidus': '棘头梅童鱼', 'Chrysochir_aureus': '黄鳍牙䱛',
           'Acheilognathus_chankaensis': '兴凯鱊', 'Konia_dikume': '迪氏康尼丽鱼', 'Sarotherodon_linnellii': '林氏帚齿非鲫',
           'Channa_argus_kimurai': '乌鳢', 'Ilisha_amazonica': '亚马逊鳓', 'Oxyurichthys_tentacularis': '触角沟虾虎鱼',
           'Pollachius_pollachius': '青鳕', 'Takifugu_rubripes_x_Takifugu_flavidus': '红鳍东方鲀_x_菊黄东方鲀',
           'Chiloscyllium_griseum': '灰斑竹鲨', 'Gymnocypris_dobula': '软刺裸鲤', 'Sinocyclocheilus_microphthalmus': '小眼金线鲃',
           'Carassius_auratus': '金鱼', 'Onychostoma_alticorpus': '高体白甲鱼', 'Brachyhypopomus_sp._n._VERD': '短身电鳗属sp._n._VERD',
           'Pampus_argenteus': '银鲳', 'Carcharhinus_amboinensis': '高鳍真鲨', 'Notropis_chlorocephalus': '绿头美洲鱥',
           'Pampus_punctatissimus': '翎鲳', 'Pimephales_sp._MCZuncat': '胖头鱥属sp. MCZuncat', 'Barbodes_lateristriga': '侧条无须魮',
           'Labeo_cf._barbatus_CBM-ZF-11784': '野鲮属cf._barbatus_CBM-ZF-11784', 'Rectoris_luxiensis': '泸溪直口鲮',
           'Rhynchocypris_oxycephalus': '尖头鱥', 'Osteobrama_cunma': 'Osteobrama_cunma(无中文名)', 'Bangana_rendahli': '华鲮',
           'Algansea_lacustris': '湖栖食草美洲鱥', 'Hemibarbus_longirostris': '长吻䱻', 'Garra_rufa': '淡红墨头鱼',
           'Hemigrammocypris_neglecta': 'Hemigrammocypris_neglecta(无中文名)', 'Phoxinus_phoxinus': '真鱥',
           'Coilia_nasus': '刀鲚', 'Distoechodon_compressus': '扁圆吻鲴',
           'Tachysurus_fulvidraco_x_Tachysurus_vachelli': '黄颡鱼 x 瓦氏黄颡鱼',
           'Takifugu_obscurus_x_Takifugu_rubripes': '暗纹东方鲀 x 红鳍东方鲀', 'Sarotherodon_galilaeus': '加利略帚齿非鲫',
           'Chanodichthys_mongolicus': '蒙古鲌', 'Osteoglossum_ferreirai': '黑骨舌鱼',
           'Channa_argus_x_Channa_maculata': '乌鳢 x 斑鳢', 'Hemiculter_bleekeri_bleekeri': '贝氏䱗',
           'Torquigener_hypselogeneion': '头纹窄额鲀', 'Setipinna_tenuifilis': '黄鲫', 'Acrossocheilus_wenchowensis': '温州光唇鱼',
           'Stolephorus_sp._CX-2021': '小公鱼属sp._CX-2021', 'Sinibrama_wui': '伍氏华鳊', 'Hemiculter_eigenmanni': '白鲦',
           'Squalidus_chankaensis': '兴凯鮈', 'Hippoglossus_hippoglossus': '庸鲽',
           'Megalobrama_skolokovii_x_Megalobrama_amblycephala': '鲂 x 团头鲂', 'Takifugu_fasciatus': '暗纹东方魨',
           'Hemiculter_bleekeri': '贝氏䱗', 'Chiloscyllium_burmensis': '缅甸斑竹鲨', 'Lutjanus_rivulatus': '蓝点笛鲷',
           'Micromesistius_poutassou': '蓝鳕', 'Puntioplites_falcifer': '镰鲃鲤', 'Channa_asiatica': '月鳢',
           'Psephurus_gladius': '白鲟', 'Discherodontus_ashmeadi': '阿氏盘齿魮', 'Carassius_sp._IDEA_Fish426': '鲫属sp._IDEA_Fish426',
           'Megalobrama_amblycephala_x_Megalobrama_skolkovii': '团头鲂 x 鲂', 'Rhinogobius_sp._OM': '吻虾虎鱼属sp._OM',
           'Rhinogobius_formosanus': '台湾吻虾虎', 'Pampus_sp._Li_et_al.,_2014': '鲳属sp._Li_et_al.,_2014',
           'Sinocyclocheilus_grahami': '滇池金线鲃', 'Paratanakia_chii': '上海齐氏副田鱊', 'Xenocypris_davidi': '黄尾鲴',
           'Acipenser_transmontanus': '高首鲟', 'Trichiurus_lepturus': '带鱼', 'Toxabramis_swinhonis': '似鱎',
           'Chanodichthys_ilishaeformis': '红鳍原鲌', 'Antimora_microlepis': '细鳞拟深海鳕', 'Siganus_fuscescens': '褐蓝子鱼',
           'Pampus_sp._Pdch1': '鲳属sp._Pdch1', 'Hypophthalmichthys_molitrix': '鲢', 'Pseudohemiculter_hainanensis': '海南拟䱗',
           'Larimichthys_polyactis': '小黄鱼', 'Sebastes_maliger': '背平鲉', 'Cyprinus_rubrofuscus': '赤棕鲤',
           'Gadus_ogac': '格陵兰鳕', 'Culter_compressocorpus': '扁体原鲌', 'Acanthochromis_polyacanthus': '多棘雀鲷',
           'diploid_Xenocypris_davidi_x_Megalobrama_amblycephala': '二倍体的黄尾鲴 x 团头鲂', 'Acipenser_medirostris': '中吻鲟',
           'Acipenser_ruthenus': '小体鲟', 'Acanthogobius_hasta': '矛尾刺虾虎鱼',
           'Rhamdia_cf._jequitinhonha_NS_3056B': '雷氏鲶属cf._jequitinhonha_NS_3056B', 'Puntius_snyderi': '史尼氏小鲃'}
# , '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': ''}

os.chdir(r'05_Feature')
dfs = glob('*.grouped.xls')
for i in dfs:
    df = pd.read_table(i)
    # for j in df['Taxonomy']:
    #     if j not in species.keys():
    #         print(j)
    df['CHName'] = df['Taxonomy'].apply(lambda x: species[x])
    df.set_index('CHName', inplace=True)
    df.to_csv(f'{i.split(".")[0]}.named.xls', encoding='utf_8_sig')
