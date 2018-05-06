# TVR's readme for https://rovitotv.github.io moving my blog to github pages.

## How to post a new article

1.  first create a file in ~/rovitotv.org/content as a mark down file, I recommend
    copying an older file

2.  Then issue the command to run pelican and re-create all new html output:
    ```bash
    make clean && make html && make serve
    ```
3.  Look at the temporary web server in your browser to make sure new post is ok
    http://100.115.92.2:8000/

4.  If the post is ok then use these commands to post to github pages:
    ```bash
    git add -A && git commit -a -m 'commit message' && git push --all
    ```

## Python packages that need to be installed on a development computer

```bash
pip install pelican
pip install markdown
pip install pelican-youtube
pip install ghp-import
```


## How to resize pictures from the command line

Note TVR has not tested on Chromebook yet, I don't know if imagemagick package
exists for Termux.

First install the convert Image Magic Command Line Utility:
```bash
sudo apt-get install imagemagick
```

To resize and image use the convert command line:
```bash
convert ESColorGuard.jpeg -resize 400x300 ESColorGuard_scaled.jpeg
```

To rotate a image us the convert command line:
```bash
convert ESColorGuard_scaled.jpeg -rotate 180 ESColorGuard_scaled_rotated.jpeg
```

## References

I followed [this blog post](https://rsip22.github.io/blog/create-a-blog-with-pelican-and-github-pages.html)
to lean how to use Pelican with github pages.