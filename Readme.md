Do uruchomienia modelu predykcyjnego potrzebujemy:
1) zainstalowanych bibliotek z requirements.txt
2) use_model.ipynb, model_epoch_307.hdf5, oraz naszej csv z przynajmniej 20 wierszami danych (oraz odpowiednimi kolumnami)
3) Dodajemy nazwe csv w use_model.ipynb i uruchamiamy: output to 0/1/2 (nie ma zagrożenia Pump&Dump, potencjalne zagrożenie, wysokie zagrożenie)
   Warto jednak zwrócić uwagę, że model zwraca często błędne dane

Model wczytuje 20 ostatnich lini, które MUSZĄ zawierać kolumny: 'Close', 'compound', 'likes', 'retweets' oddzielone przecinkiem.
