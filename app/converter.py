from selenium import webdriver
from selenium.webdriver.common.by import By
from data import InputData
import torch


class Converter:
    def __init__(self, tokenizer, model):
        self.tokenizer = tokenizer
        self.model = model

    def collect_elements(self, data: InputData):
        driver = self.__set_browser(data.browser)
        driver.get(data.url)

        elements = []

        if data.h:
            headers = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
            for header in headers:
                elements.extend(driver.find_elements(By.TAG_NAME, header))

        if data.p:
            elements.extend(driver.find_elements(By.TAG_NAME, 'p'))

        for element in elements:
            if len(element.text.split()) >= data.length_min:
                driver.execute_script("arguments[0].textContent = arguments[1];",
                                      element, self.__convert(element.text, data.length_max))

    def __set_browser(self, browser):
        driver = webdriver.Chrome()
        match browser:
            case "Firefox":
                driver = webdriver.Firefox
            case "Safari":
                driver = webdriver.Safari
        return driver

    def __convert(self, text, max_length):
        device = "cuda:0" if torch.cuda.is_available() else "cpu"
        inputs = self.tokenizer(text, max_length=1024, return_tensors='pt', truncation=True).to(device)
        model = self.model.to(device)
        summary_ids = model.generate(inputs['input_ids'], num_beams=4, max_length=max_length, early_stopping=True)
        summary = [self.tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in
                   summary_ids]

        return summary

    def __read_file_to_list(self, file_path):
        with open(file_path, 'r', encoding="utf-8") as file:
            lines = [line for line in file.read().split('\n') if line]
        return lines

    def save_to_file(self, data: InputData):
        lines = self.__read_file_to_list(data.file_path)
        with open(data.save_path, 'w', encoding="utf-8") as f:
            for item in lines:
                if len(item.split()) > data.length_min:
                    converted_text = self.__convert(item, max_length=data.length_max)
                    f.write(converted_text[0] + "\n\n")
                else:
                    f.write(item + "\n")
