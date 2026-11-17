# Elevator Queue Lab

A standalone page for exploring how an elevator controller orders its queue, in normal and Shabbat mode. Place
people waiting at floors and watch which floor the car is sent to next, and why.

Everything runs in the browser: no server, no sign-in. Your list of people is kept in your own browser's local
storage.

## Updating

`index.html` is built from `web/elevator-queue-lab.html` in the FaceRecognition project (the source of truth):

```
python build.py
git commit -am "Update the Queue Lab"
git push
```
