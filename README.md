# wedding
Code for wedding directory.

## Required Packages

We need [ImageMagick](https://imagemagick.org/) and [Potrace](http://potrace.sourceforge.net/).

Installation directions for ImageMagick can be found on their [download site](https://imagemagick.org/script/download.php).  Alternatively, you can download the MacOS version with with [this link](https://imagemagick.org/download/binaries/ImageMagick-x86_64-apple-darwin19.0.0.tar.gz).  Extract the contents and set the `MAGICK_HOME` environment variable to the extracted path.  Similary add the `bin` subdirectory to `PATH` and the `lib` subdirectory to `DYLD_LIBRARY_PATH`.

```
export MAGICK_HOME="$HOME/ImageMagick-7.0.9"
export PATH="$MAGICK_HOME/bin:$PATH"
export DYLD_LIBRARY_PATH="$MAGICK_HOME/lib:$DYLD_LIBRARY_PATH"
```

We can download the MacOS versio of Potrace with [this link](http://potrace.sourceforge.net/download/1.16/potrace-1.16.mac-x86_64.tar.gz).  Extract potrace and add its directory to `PATH`.

```
export PATH="$HOME/potrace-1.16.mac-x86_64:$PATH"
```

It should be noted that all of these programs are third-party apps, and you will need to make sure that your MacOS will allow third-party apps.  Directions can be found [here](https://www.geekrar.com/how-to-allow-third-party-apps-install-on-macos-catalina/) for enabling permission on Catalina.  Basically on terminal, input

```
sudo spctl --master-disable
```


## Creating Environment with Required Packages

Let's be clean about it.

```
conda create -n wedding python=3.5 anaconda
conda activate wedding

conda install -n wedding -c menpo opencv
```

## Creating SVG from JPG

To do this, we

```
convert image.png image.ppm
potrace -s image.ppm -o image.svg
```


