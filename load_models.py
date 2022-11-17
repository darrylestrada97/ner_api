

import tensorflow as tf



enfermedad = tf.keras.models.load_model('enfermedad/model-complete')
farmaco = tf.keras.models.load_model('farmaco/model-complete')

def get_predict(modelname, x ):
    if modelname == "enfermedad":
        return enfermedad.predict(x)
    if modelname == "farmaco":
        return farmaco.predict(x)
    