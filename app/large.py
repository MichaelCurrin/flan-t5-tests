from transformers import T5Tokenizer, T5ForConditionalGeneration


tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-large")
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-large")

print("TRANSLATE")
input_text = "translate English to German: How old are you?"
input_ids = tokenizer(input_text, return_tensors="pt").input_ids

outputs = model.generate(input_ids)
print(tokenizer.decode(outputs[0]))
# <pad> Wie alte sind Sie?</s>

print("---")
print("SUMMARIZE")

content = """\
The tower is 324 metres (1,063 ft) tall, about the same height as
an 81-storey building, and the tallest structure in Paris. Its base is square,
measuring 125 metres (410 ft) on each side. It was the first structure to reach
a height of 300 metres. Excluding transmitters, the Eiffel Tower is the second
tallest free-standing structure in France after the Millau Viaduct.
"""

input_text = f"summarize: {content}"
input_ids = tokenizer(input_text, return_tensors="pt").input_ids

outputs = model.generate(input_ids)
print(tokenizer.decode(outputs[0]))
# <pad> The Eiffel Tower is the tallest free-standing structure in France.</s>

print("Expected:")
print(
    "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building. It was the first structure to reach a height of 300 metres."
)
