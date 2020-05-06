import csv

import pystache

csv_columns = ['name', 'Streaming', 'Name', 'NAME', 'enable', 'ticker', 'orderbook', 'refresh_rate']
csv_file = "data.csv"

output_dir = "output/"

factory_java_template = "templates/factoryJava.tpl"
factory_streaming_java_template = "templates/factoryJavaStreaming.tpl"

pom_template_file = "templates/pom.tpl"
pom_file = "pom.xml"

main_java_template_file = "templates/main_java.tpl"
main_streaming_java_template_file = "templates/main_streaming_java.tpl"
main_file = "main.java"

ExchangesFactory_template_file = "templates/Exchanges_factory_java.tpl"
ExchangesFactory_file = "ExchangesFactory.java"

Exchanges_java_template_file = "templates/exchanges_java.tpl"
Exchanges_streaming_java_template_file = "templates/exchanges_streaming_java.tpl"

constants_template_file = "templates/constants.tpl"
constants_streaming_template_file = "templates/constants_streaming.tpl"
constants_file = "Constants.java"

properties_template_file = "templates/properties.tpl"
properties_file = "config.properties"

entrypoint_template_file = "templates/EntryPoint.tpl"
entrypoint_enum_template_file = "templates/EntryPoint_enum.tpl"
entrypoint_switch_template_file = "templates/EntryPoint_switch.tpl"
entrypoint_file = "EntryPoint.java"
entrypoint_enum_file = "EntryPoint_enum.java"
entrypoint_switch_file = "EntryPoint_switch.java"

bus_definition_template_file = "templates/bus_definition.tpl"
bus_definition_template_file2 = "templates/bus_definition2.tpl"
bus_definition_template_file3 = "templates/bus_definition3.tpl"
bus_definition_file = "bus_definition.java"
bus_definition_file2 = "bus_definition2.java"
bus_definition_file3 = "bus_definition3.java"


def feeder(arr):
    factory_java = ''
    f = open(factory_java_template, mode='r')
    if f.mode == 'r':
        factory_java = f.read()

    factory_streaming_java = ''
    f = open(factory_streaming_java_template, mode='r')
    if f.mode == 'r':
        factory_streaming_java = f.read()

    pom_xml = ''
    f = open(pom_template_file, mode='r')
    if f.mode == 'r':
        pom_xml = f.read()

    main_java_template = ''
    f = open(main_java_template_file, mode='r')
    if f.mode == 'r':
        main_java_template = f.read()

    main_streaming_java_template = ''
    f = open(main_streaming_java_template_file, mode='r')
    if f.mode == 'r':
        main_streaming_java_template = f.read()

    ExchangesFactory_template = ''
    f = open(ExchangesFactory_template_file, mode='r')
    if f.mode == 'r':
        ExchangesFactory_template = f.read()

    Exchanges_java_template = ''
    f = open(Exchanges_java_template_file, mode='r')
    if f.mode == 'r':
        Exchanges_java_template = f.read()

    Exchanges_streaming_java_template = ''
    f = open(Exchanges_streaming_java_template_file, mode='r')
    if f.mode == 'r':
        Exchanges_streaming_java_template = f.read()

    constants_template = ''
    f = open(constants_template_file, mode='r')
    if f.mode == 'r':
        constants_template = f.read()

    constants_streaming_template = ''
    f = open(constants_streaming_template_file, mode='r')
    if f.mode == 'r':
        constants_streaming_template = f.read()

    properties_template = ''
    f = open(properties_template_file, mode='r')
    if f.mode == 'r':
        properties_template = f.read()

    entrypoint_template = ''
    f = open(entrypoint_template_file, mode='r')
    if f.mode == 'r':
        entrypoint_template = f.read()

    entrypoint_enum_template = ''
    f = open(entrypoint_enum_template_file, mode='r')
    if f.mode == 'r':
        entrypoint_enum_template = f.read()

    entrypoint_switch_template = ''
    f = open(entrypoint_switch_template_file, mode='r')
    if f.mode == 'r':
        entrypoint_switch_template = f.read()

    pom_output = open(output_dir + pom_file, "w+")
    main_output = open(output_dir + main_file, "w+")
    ExchangesFactory_output = open(output_dir + ExchangesFactory_file, "w+")
    constants_output = open(output_dir + constants_file, "w+")
    properties_output = open(output_dir + properties_file, "w+")
    entrypoint_output = open(output_dir + entrypoint_file, "w+")
    entrypoint_enum_output = open(output_dir + entrypoint_enum_file, "w+")
    entrypoint_switch_output = open(output_dir + entrypoint_switch_file, "w+")

    for rows in arr:
        factory_output = open(output_dir + rows[csv_columns[2]] + "Factory.java", "w+")
        exchanges_output = open(output_dir + rows[csv_columns[2]] + ".java", "w+")
        if rows[csv_columns[1]] == 'y':
            factory_output.write(pystache.render(factory_streaming_java, rows))
            main_output.write(pystache.render(main_streaming_java_template, rows))
            exchanges_output.write(pystache.render(Exchanges_streaming_java_template, rows))
            constants_output.write(pystache.render(constants_streaming_template, rows))
        else:
            factory_output.write(pystache.render(factory_java, rows))
            main_output.write(pystache.render(main_java_template, rows))
            exchanges_output.write(pystache.render(Exchanges_java_template, rows))
            constants_output.write(pystache.render(constants_template, rows))
        factory_output.close()
        pom_output.write(pystache.render(pom_xml, rows))
        exchanges_output.close()
        properties_output.write(pystache.render(properties_template, rows))
        ExchangesFactory_output.write(pystache.render(ExchangesFactory_template, rows))
        entrypoint_output.write(pystache.render(entrypoint_template, rows))
        entrypoint_enum_output.write(pystache.render(entrypoint_enum_template, rows))
        entrypoint_switch_output.write(pystache.render(entrypoint_switch_template, rows))
    pom_output.close()
    ExchangesFactory_output.close()
    properties_output.close()


def recorder(arr):
    bus_definition_template = ''
    f = open(bus_definition_template_file, mode='r')
    if f.mode == 'r':
        bus_definition_template = f.read()

    bus_definition_template2 = ''
    f = open(bus_definition_template_file2, mode='r')
    if f.mode == 'r':
        bus_definition_template2 = f.read()

    bus_definition_template3 = ''
    f = open(bus_definition_template_file3, mode='r')
    if f.mode == 'r':
        bus_definition_template3 = f.read()

    bus_definition_output = open(output_dir + bus_definition_file, "w+")

    bus_definition_output2 = open(output_dir + bus_definition_file2, "w+")

    bus_definition_output3 = open(output_dir + bus_definition_file3, "w+")

    for rows in arr:
        bus_definition_output.write(pystache.render(bus_definition_template, rows))
        bus_definition_output2.write(pystache.render(bus_definition_template2, rows))
        bus_definition_output3.write(pystache.render(bus_definition_template3, rows))

    bus_definition_output.close()
    bus_definition_output2.close()
    bus_definition_output3.close()


'''
source : https://stackoverflow.com/questions/14158868/python-skip-comment-lines-marked-with-in-csv-dictreader
'''


def decomment(csvfile):
    for row in csvfile:
        raw = row.split('#')[0].strip()
        if raw: yield row


'''
MAIN
'''


def main():
    arr = []
    with open(csv_file, mode='r') as infile:
        reader = csv.reader(decomment(infile), delimiter=';')
        for rows in reader:
            mydict = {csv_columns[0]: rows[0], csv_columns[1]: rows[1],
                      csv_columns[2]: rows[0].capitalize(), csv_columns[3]: rows[0].upper(),
                      csv_columns[4]: rows[2], csv_columns[5]: rows[3], csv_columns[6]: rows[4],
                      csv_columns[7]: rows[5]}
            arr.append(mydict)
    #feeder(arr)
    recorder(arr)


if __name__ == '__main__':
    main()
