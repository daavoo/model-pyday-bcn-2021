# dataset-pyday-bcn-2021

<details>
<summary>0. Repo setup (already run for you)
</summary>

```
git clone git@github.com:daavoo/dataset-pyday-bcn-2021.git
cd dataset-pyday-bcn-2021
```

```
pip install -r requirements.txt
```

```
dvc init
```

</details>

---

You should be able to follow all the steps bellow without leaving the browser.

---

## 1. Fork this repo

- https://github.com/daavoo/dataset-pyday-bcn-2021

---

## 2. Run `Import Dataset` Workflow


<details>
<summary>Create `secrets.GDRIVE_CREDENTIALS_DATA`</summary>

- Get the credentials:
https://colab.research.google.com/drive/1Xe96hFDCrzL-Vt4Zj-cVHOxUgu-fyuBW

- Add new secret to GitHub repo.

</details>

- Go to `Actions` -> `Import Dataset` -> `Run Workflow`.

## 3. Run `Train` Workflow

- Go to `Actions` -> `Train` -> `Run Workflow`.
