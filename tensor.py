import tensorflow as tf
from tensorflow.keras import layers

# 1. Load and preprocess data (example using a pre-loaded dataset)
# (X_train, y_train), (X_test, y_test) = ... load your dataset ...

# 2. Build a lightweight model (MobileNetV2 backbone)
base_model = tf.keras.applications.MobileNetV2(input_shape=(224, 224, 3),
                                               include_top=False,
                                               weights='imagenet')
base_model.trainable = False # Transfer Learning

model = tf.keras.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(3, activation='softmax') # 3 classes
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 3. Train the model
# model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# 4. Convert to TensorFlow Lite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the model.
with open('recyclable_model.tflite', 'wb') as f:
    f.write(tflite_model)

# 5. Test the TFLite model (Optional: Do this on a Raspberry Pi)
interpreter = tf.lite.Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# ... (Run inference on a test image and print results) ...
