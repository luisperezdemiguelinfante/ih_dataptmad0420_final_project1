import argparse
from modules import m_acquisition
from modules.as_is_excel import m_alcance_analisis, m_vision_global, m_procesos, m_distribucion_process_site
from modules.as_is_charts import m_vision_global_fig, m_fig_excel
from modules.to_be import to_be_template, field_prediction, field4_prediction, operative_prediction
import pandas as pd


def to_excel(df_dict: dict, excel_name: str) -> None:
    with pd.ExcelWriter(excel_name) as writer:
        for df, sheet in df_dict.items():
            df.to_excel(writer, sheet_name=sheet)


def argument_parser():
    parser = argparse.ArgumentParser(description='sepcify company..')
    #parser.add_argument("-e", "--empresa", type = str, help='specify the company...', required=True)
    args = parser.parse_args()

    return args


def main(empresa):
    print('starting pipeline...')

    template = m_acquisition.plantilla(empresa)
    alcance= m_alcance_analisis.alcance_analisis(template)
    procesos_site = m_procesos.process_site_split(template)
    vision_global = m_vision_global.empleado_dedicacion(template)
    tareas_process = m_distribucion_process_site.tareas_proceso(template)
    vision_global_fig = m_vision_global_fig.vision_global_fig(template)
    excel_charts= m_fig_excel.excel_chart(template)
    #key_words_template=key_words.key_words_column(template)
    eficiencias_totales=to_be_template.to_be_eficiencias(template)
    field_predictions=field_prediction.field_labels(template)
    field4_predictions=field4_prediction.field4_labels(template)
    operative_predictions= operative_prediction.operative_labels(template)

    #df_dict_vision_global = m_vision_global.empleado_dedicacion(template)
    #df_alcance_analisis = m_alcance_analisis.alcance_analisis(template)

    #assert type(df_dict_vision_global) == dict
    #assert type(df_alcance_analisis) == dict

    #df_dict_global = dict(**df_dict_vision_global, **df_alcance_analisis)

    #print(list(df_dict_global.keys()), list(df_dict_global.values()))

    #assert type(df_dict_global) == dict

    #to_excel(df_dict_global, 'as_is_excel_test.xlsx')

    return template, vision_global, alcance,procesos_site, tareas_process, vision_global_fig, excel_charts, eficiencias_totales, field_predictions, field4_predictions, operative_predictions



if __name__ == '__main__':
    arguments = argument_parser()
    main(arguments)

