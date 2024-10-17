import torch
import torch.nn as nn
from transformers import BartTokenizer, BartForConditionalGeneration

class Summary_brief(nn.Module):
    def __init__(self, model_name='facebook/bart-large-cnn'):
        super(Summary_brief, self).__init__()

        self.model = BartForConditionalGeneration.from_pretrained(model_name)
        self.text_tokenizer = BartTokenizer.from_pretrained(model_name)

    def forward(self, input_ids, attention_mask=None):
        outputs = self.model(input_ids=input_ids, attention_mask=attention_mask)
        return outputs.logits

    def summarize(self, text, max_length=150, min_length=40):
        # Tokenizing input text
        inputs = self.text_tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)

        # Summmary generation
        summarizer = self.model.generate(inputs['input_ids'],
                                          attention_mask=inputs['attention_mask'],
                                          max_length=max_length,
                                          min_length=min_length,
                                          length_penalty=2.0,
                                          num_beams=4,
                                          early_stopping=True)
        if summarizer is not None and len(summarizer) > 0:

            summary = self.text_tokenizer.decode(summarizer[0], skip_special_tokens=True)
            return summary



if __name__=="__main__":
    model = Summary_brief()






