# -*- coding: utf-8 -*- 
import io
from app import model, tokenizer, device

def resumir(text):   
    # tokenizer recibe el string y entrega inputs_ids y attention_mask, que son Tensor, el tipo que usa Pytorch para los vectores / tensores
    inputs = tokenizer([text], padding="max_length", truncation=True, max_length=512, return_tensors="pt")
    input_ids = inputs.input_ids.to(device)
    attention_mask = inputs.attention_mask.to(device)

    # llamar al modelo que entrega tensores
    output = model.generate(input_ids, attention_mask=attention_mask)

    # decodificar el resultado con el tokenizer
    resumen = tokenizer.decode(output[0], skip_special_tokens=True)
    return resumen
