# AI Image Classifier

## O projektu

Ova aplikacija omogućava korisnicima da učitaju bilo koju sliku i uz pomoć veštačke inteligencije saznaju šta se na njoj nalazi. Interfejs je napravljen kao veb aplikacija, dok se u pozadini koristi moćan sistem za kompjuterski vid kako bi se slika obradila i klasifikovala. 

Projekat je savršen primer implementacije predtreniranih modela dubokog učenja u moderno korisničko okruženje.

## Funkcionalnosti

**Grafički veb interfejs**
Aplikacija je laka za korišćenje. Kroz čist Streamlit interfejs, korisnik može jednostavno prevući i ubaciti sliku u formatu JPG ili PNG.

**Visoka preciznost prepoznavanja**
Korišćenjem MobileNetV2 arhitekture trenirane na ogromnoj ImageNet bazi podataka, model prepoznaje hiljade različitih objekata i vraća tri najverovatnija rezultata sa procentom sigurnosti.

**Optimizovane performanse**
Zahvaljujući ugrađenom mehanizmu keširanja, teški AI model se učitava samo jednom prilikom pokretanja aplikacije. Svaka sledeća slika se analizira gotovo trenutno.

## Korišćene tehnologije

Projekat je napisan u **Python** programskom jeziku.
Korisnički interfejs je kreiran pomoću okvira **Streamlit**.
Logika mašinskog učenja oslanja se na **TensorFlow** i **Keras** (MobileNetV2).
Za obradu i pripremu slika pre slanja u model korišćeni su **OpenCV**, **NumPy** i **Pillow (PIL)**.

## Instalacija i pokretanje

Za lokalno pokretanje ove aplikacije, potrebno je ispratiti sledeće korake.

1. Kloniraj repozitorijum:
```bash
git clone [https://github.com/TvojUsername/ime-repozitorijuma.git](https://github.com/TvojUsername/ime-repozitorijuma.git)
cd ime-repozitorijuma
