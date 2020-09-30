from src.AIs.models.TestModel.TestModel import TestModel

ai_network = TestModel(
    mode="TEST_TACTICS",
    epochs=1,
    players=1
)

result = ai_network.test_get_result()
for i in result:
    print(i)
