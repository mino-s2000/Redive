import codecs
import yaml
import json

def convert_chara_name_to_id(c_name):
    # yamlにする
    if c_name == 'ミヤコ':
        return 'miyako_basic'
    else:
        return 'miyako_basic'

def get_chara_data(c_name):
    c_id = convert_chara_name_to_id(c_name)
    with codecs.open(f'.\\character\\{c_id}.jp.yml', 'r', 'utf-8') as f:
        return yaml.load(f)

def get_character(msg):
    c = get_chara_data(msg[3])
    reply = ''
    if msg[2] == 'information' or msg[2] == 'info':
        c_info = c["information"]
        row1 = f'ポジション: {c_info["position"]}\n'
        row2 = f'攻撃種別: {c_info["attacking_category"]}\n'
        row3 = f'役割: {c_info["role"]}\n'
        row4 = f'初期レア度: {c_info["default_rarity"]}\n'
        row5 = f'種族: {c_info["breed"]}\n'
        row6 = f'メモリーピース取得方法: {c_info["get_memory_piece"]}\n'
        reply = f'```{row1}{row2}{row3}{row4}{row5}{row6}```'
    elif msg[2] == 'status':
        c_status = c["maximum_status"]
        c_offensive_strength = c_status["strength"]["offensive"]
        c_defensive_strength = c_status["strength"]["defensive"]
        row1 = '※ Lv.118, Rank 12, 装備強化最大, 初期レアリティ\n'
        row2 = f'HP: {c_status["hp"]}\n'
        row3 = f'物理攻撃力: {c_offensive_strength["physical"]}\n'
        row4 = f'魔法攻撃力: {c_offensive_strength["magical"]}\n'
        row5 = f'物理防御力: {c_defensive_strength["physical"]}\n'
        row6 = f'魔法防御力: {c_defensive_strength["magical"]}\n'
        reply = f'```{row1}{row2}{row3}{row4}{row5}{row6}```'
    elif msg[2] == 'skill':
        c_skill = c["skill"]
        print(json.dumps(c_skill,ensure_ascii=False,indent=2))
        reply = '準備中...'
    else:
        reply = 'Second option is ignore.'
    return reply
