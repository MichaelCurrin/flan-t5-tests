"""
Generic model demo script.

Based on the other script, this code is DRY and accepts CLI params.
"""

import os
import sys

from transformers import T5Tokenizer, T5ForConditionalGeneration


def load_model(model_name: str) -> tuple:
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)

    return tokenizer, model


def generate_output(tokenizer, model, input_text: str) -> str:
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    outputs = model.generate(input_ids)

    return tokenizer.decode(outputs[0], skip_special_tokens=True)


def run(model_id: str, task: str, content: str) -> str:
    tokenizer, model = load_model(model_id)

    return generate_output(tokenizer, model, f"{task}: {content}")


def main(args) -> None:
    if len(args) != 4:
        name = os.path.basename(__file__)
        print(f"Usage: python {name} MODEL_ID TASK CONTENT")
        print(
            f"  e.g. python {name} 'google/flan-t5-small' 'translate English to German' 'How old are you?'"
        )
        sys.exit(1)

    model_id = args[1]
    task = args[2]
    content = args[3]

    result = run(model_id, task, content)
    print(result)


if __name__ == "__main__":
    main(sys.argv)
