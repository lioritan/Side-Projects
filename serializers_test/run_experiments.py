import avro_avg
import message_generator
import serialization
import pandas as pd
import numpy as np
from time import time
import avro.io
import avro_small
import avro_big


def run_experiment(generator_func, avro_schema, times=100):
    results = np.zeros((times, 8))
    for i in range(times):
        print(i)
        results[i, :] = run_single(generator_func, avro_schema)
    df = pd.DataFrame(data=results, columns=["avro_ser_time", "avro_deser_time", "avro_total_time", "avro_ser_size",
                                             "proto_ser_time", "proto_deser_time", "proto_total_time",
                                             "proto_ser_size"])
    return df


def run_single(generator_func, avro_schema):
    results = np.zeros(8)

    message_proto, message_dict = generator_func()
    datum_writer = avro.io.DatumWriter(avro_schema)
    datum_reader = avro.io.DatumReader(avro_schema)

    before_ser = time()
    serialized = serialization.serialize_avro_to_string(datum_writer, message_dict)
    results[0] = time() - before_ser
    before_deser = time()
    deserialized = serialization.deserialize_string_to_avro(datum_reader, serialized)
    results[1] = time() - before_deser
    results[2] = results[0] + results[1]
    results[3] = len(serialized)

    before_ser = time()
    serialized = serialization.serialize_proto_to_string(message_proto)
    results[4] = time() - before_ser
    message_proto.Clear()
    before_deser = time()
    serialization.deserialize_string_to_proto(serialized, message_proto)
    results[5] = time() - before_deser
    results[6] = results[4] + results[5]
    results[7] = len(serialized)

    return results


ppp = run_experiment(message_generator.create_small_message, avro_small.avro_schema, 1000)
ppp.to_csv(path_or_buf="small_numbers.csv")
ppp2 = run_experiment(message_generator.create_avg_message, avro_avg.avro_schema, 1000)
ppp2.to_csv(path_or_buf="avg_numbers.csv")
ppp3 = run_experiment(message_generator.create_big_message, avro_big.avro_schema, 100)
ppp3.to_csv(path_or_buf="big_numbers.csv")
aa = 4
