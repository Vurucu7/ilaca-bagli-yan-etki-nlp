# 💊 İlaca Bağlı Yan Etki Örüntüsü - NLP Projesi

Bu proje, **openFDA Adverse Event** veri seti kullanılarak, kullanıcıların bildirdiği yan etkiler ile ilaçlar arasında **metin benzerliğine** dayalı örüntü eşleştirmesi yapılmasını hedeflemektedir. Çalışma kapsamında doğal dil işleme teknikleriyle metin temizleme, **Zipf analizi**, **TF-IDF** ve **Word2Vec** tabanlı vektörleştirme işlemleri gerçekleştirilmiştir.

---

## 📁 Veri Seti Bilgisi

- **Kaynak**: [openFDA Adverse Event Data](https://open.fda.gov/data/download/)
- **Dosya**: `drug-event-0016-of-0034.json`
- **Format**: JSON
- **Boyut**: ~1.7 MB
- **Kullanılan Alan**: `patient.reaction[].reactionmeddrapt`
- **Amaç**: Yan etki metinlerini vektörleştirerek semantik analiz yapmak

---
Proje dosya açıklamaları:
preprocessing.py --->Lemmatization ve stemming işlemleri uygular, CSV çıktıları üretir
zipfYasasi.py --->	Ham veri üzerinde Zipf log-log grafiği çizer
tf_idf_Vektor.py --->	Lemmatize ve stemlenmiş veriler için TF-IDF matrislerini üretir
word2vec_train.py --->	8 farklı parametre seti ile 16 Word2Vec modeli eğitir
word2vec_test_similar.py --->	Her modelden bir kelimeye en yakın 5 kelimeyi yazdırır
zipf_graph_stem_lemma.py --->	Lemma ve stem dosyaları için ayrı Zipf grafikleri çizer

## ⚙️ Kurulum

Projeyi çalıştırmak için gerekli tüm Python kütüphanelerini şu komutla yükleyebilirsiniz:

```bash
pip install pandas numpy matplotlib nltk scikit-learn gensim

⚠️ Not: Model dosyaları büyük boyutlu olduğundan GitHub'a yüklenmemiştir. Eğitim kodları mevcuttur.

⚠️ Not: `tfidf_lemmatized.csv` ve `tfidf_stemmed.csv` dosyaları boyut sınırını aştığı için GitHub’a yüklenmemiştir. 
Bu dosyalar `tf_idf_Vektor.py` kodu çalıştırıldığında otomatik olarak oluşturulmaktadır.
# Doğal Dil İşleme Ödevi 2  
**Eğitilen Modellerle Metin Benzerliği Hesaplama ve Değerlendirme**

---
Ödev 2
## 📚 Proje Açıklaması

Bu projede, ön işleme tabi tutulmuş reçete metinlerinden oluşan veri seti üzerinde TF-IDF ve Word2Vec modelleriyle metin benzerliği analizleri yapılmıştır. Modellerin çıktıları değerlendirilmiş, farklı teknikler karşılaştırılmıştır.

---

## 📁 Dosya ve Klasör Yapısı

- `lemmatized_output.csv`   # Lemmatize edilmiş veri seti  
- `stemmed_output.csv`      # Stem edilmiş veri seti  
- `tfidf_lemmatized.csv`     # Lemmatize veri için TF-IDF vektörleri  
- `tfidf_stemmed.csv`       # Stemmed veri için TF-IDF vektörleri  
- `tfidf_similarity_analysis.py` # TF-IDF ile benzerlik analiz kodu  
- `tfidf_similarity_results.csv` # TF-IDF benzerlik sonuçları  
- `word2vec_train.py`       # Word2Vec model eğitim kodu  
- `word2vec_similarity_analysis.py` # Word2Vec ile benzerlik analiz kodu  
- `word2vec_similarity_results.csv` # Word2Vec benzerlik sonuçları  
- (Diğer yardımcı scriptler ve görseller)

---

## 🛠️ Gereksinimler ve Kurulum

Çalışma için aşağıdaki Python kütüphaneleri gereklidir:
- Python 3.8+
- pandas
- numpy
- gensim
- scikit-learn

Gerekli kütüphaneleri yüklemek için:
```bash
pip install pandas numpy gensim scikit-learn
