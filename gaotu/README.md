# Physics practice: Lessons 7–11

Open `physics_practice.html` in a browser. It includes 25 exercises, original diagrams, and step-by-step solutions. Use the hamburger menu to switch between English and Chinese. The page works offline and supports search and printing.

The five PDFs are the source worksheets. The worked solutions were derived for this workbook; they are not official source answer keys.

To rebuild the standalone HTML, install Python 3 and Poppler (`pdftoppm`), then run from this folder:

```sh
python3 work/build_practice.py
```

The builder uses `work/english_content.py` for English translations and embeds `work/practice.js` in the final HTML. Generated diagrams and previews are ignored by Git.
