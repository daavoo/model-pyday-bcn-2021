# model-pyday-bcn-2021

<details>
<summary>0. Repo setup (already run for you)
</summary>

```
git clone git@github.com:daavoo/model-pyday-bcn-2021.git
cd model-pyday-bcn-2021
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

- https://github.com/daavoo/model-pyday-bcn-2021

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

- Edit `params.yaml` from the GitHub Interface.

- Change `learning_rate`.

- Select `Create a new branch for this commit and start a pull request`

---

## Bonus: Operation Vacation

- Update `Train` workflow to run on cron schedule.

![imagen](https://user-images.githubusercontent.com/12677733/143140752-e445b36a-5fe1-4ccb-88bb-a7fa7a88f18c.png)


## Bonus: Run Pipeline from Studio

- https://studio.iterative.ai

- Access studio view: https://dvc.org/doc/studio/get-started

- Run the pipeline editing the params: https://dvc.org/doc/studio/user-guide/run-experiments
