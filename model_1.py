from owlready2 import *

def model_1():
    onto = get_ontology("../model_repostory/model_2.owl")
    onto.load()

    onto.m.input_value = (float(onto.WICQst_st.param_value) + float(onto.WICQst_nd.param_value)) / 2
    value = (float(onto.mu.input_value) * float(onto.M_ZnO.input_value) * float(onto.Ch.input_value)) / (
                1000 * float(onto.alpha.input_value) * float(onto.M_H.input_value) * float(onto.m.input_value))
    print(value)
    onto.beta.output_value = value

model_1()