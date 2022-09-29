import torch
from transformers import PreTrainedTokenizerFast
from transformers import BartForConditionalGeneration

def summarization_text(text):
    tokenizer = PreTrainedTokenizerFast.from_pretrained('alaggung/bart-r3f')
    model = BartForConditionalGeneration.from_pretrained('alaggung/bart-r3f')

    raw_input_ids = tokenizer.encode(text)
    input_ids = [tokenizer.bos_token_id] + raw_input_ids + [tokenizer.eos_token_id]

    summary_ids = model.generate(torch.tensor([input_ids]))
    return tokenizer.decode(summary_ids.squeeze().tolist(), skip_special_tokens=True)
