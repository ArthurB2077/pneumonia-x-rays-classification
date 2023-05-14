from model_loader import ModelLoader


print("\033[91m=====================================================================\033[0m")
print("\033[91m****************************INFERENCE LOGS****************************\033[0m")
print("\033[91m===================================================================\033[0m\n")

model = ModelLoader(btch_size=32,img_size=(256, 256))
model.load('notebooks/5_regularization/model_5.keras')
model.evaluate()
model.predict(img_size=(256, 256))

print("\n\033[91m===================================================================\033[0m")
print("\033[91m****************************INFERENCE LOGS****************************\033[0m")
print("\033[91m===================================================================\033[0m")