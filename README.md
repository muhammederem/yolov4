# YOLOV4 ile Custom Object Detection

Bu repoda yolov4 kullanarak istediğimiz nesneyi tanıyabileceğimiz bir model eğitmeyi baştan sonra göreceğiz.

## Gerekli olanlar

Öncelikle eğitim yapacağımız nesneyi belirliyoruz.

[Veri Seti](https://www.kaggle.com/olgabelitskaya/the-dataset-of-flower-images/data)'ne buradan ulaşabiliriz.

Daha sonra fotoğrafları etiketlemek için [LabelImg](https://github.com/tzutalin/labelImg) reposunu kullanacağız.

Bu repoyu önce bir klasöre klonlayacağız daha sonra ise pyQt ile oluşturulmuş uygulamayı kullanabilmek için aşağıdaki adımları izleyeceğiz.

### Ubuntu Linux

```python
sudo apt-get install pyqt5-dev-tools
sudo pip3 install -r requirements/requirements-linux-python3.txt
make qt5py3
python3 labelImg.py
python3 labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
```
### MacOS

```python
brew install qt  # Install qt-5.x.x by Homebrew
brew install libxml2

or using pip

pip3 install pyqt5 lxml # Install qt and lxml by pip

make qt5py3
python3 labelImg.py
python3 labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
```
### Windows
Windows için önce [PyQt5](https://www.riverbankcomputing.com/software/pyqt/download5) ve [lxml](http://lxml.de/installation.html) indiriyoruz. Daha sonra repoyu kopyaladığımız dosya konumuna gidip aşağıdaki komutları çalıştırıyoruz.
```python
pyrcc4 -o libs/resources.py resources.qrc
For pyqt5, pyrcc5 -o libs/resources.py resources.qrc

python labelImg.py
python labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
```
