# TEXT SUMMARIZER

  Aplikacja pozwalająca na podsumowywanie tekstu z plików oraz stron internetowych

## METRYKI:
  Użyte modele:
  - [Falconsai/text_summarization](https://huggingface.co/Falconsai/text_summarization)
  - [facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn)
  - [csebuetnlp/mT5_multilingual_XLSum](https://huggingface.co/csebuetnlp/mT5_multilingual_XLSum)

  Użyte metryki:
  - Rouge Score
  - Bert Score
    
  Sposób ich porównania można znaleźć tutaj: [METRYKI](https://colab.research.google.com/drive/1jseNEfOUymg-KgbSx9fOS4wNCbg-s9wn?usp=sharing)</br>
  Rezultaty są dostępne tutaj [metrics.txt](metric_results)

## UŻYTKOWANIE:

  Biblioteki wymagane do odpalenia projektu znajdują się w pliku requirements.txt

  Po zainstalowaniu wszystkich wymaganych bibliotek w konsoli musimy wpisać
```
python3 <PATH>\app\main.py
```
Aplikacja posiada dwie możliwości podsumowywań tekstu:
  - poprzez przeglądarkę
  - poprzez załadowanie pliku tekstowego
</br>
Każda z opcji posiada kilka ustawień:</br>
</br>
Przeglądarka:</br>
  - Enter url -> W tym polu podajemy url strony, którą chcemy streścić</br>
  - Content->  Wybieramy tagi, które chcemy streścić (aktualnie dostępne paragrafy oraz wszystkie headery)</br>
  - Minimal content length ->  Minimalna ilośc słów, którą chcemy streścić</br>
  - Maxiam summarized content length -> Maksymalna ilość znaków, którą chcemy przeznaczyć na streszczenia</br>
  - Select browser -> Wybieramy przeglądarkę, w której ma otworzyć się nam strona (zalecany Chrome)</br>
  </br>
Pliki tekstowe:</br>
  - File path -> Ścieżka do pliku, który chcemy streścić</br>
  - Save path -> Ścieżka do miejsca, którym zostanie zapisany nasz plik (Ścieżka wraz z nazwą pliku)</br>

### ZALECANE JEST UŻYWANIE GPU, GDYŻ ZNACZNIE SKRACA TO CZAS SUMARYZACJI TEKSTU
