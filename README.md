## Create new plotly env

```
cd ../..
```
Create conda env
```
sudo conda create -y -p home/shared-v2/custom-kernels/conda-envs/<CONDA_ENV_NAME> python=3.8 dash=2.0.0 dash-bootstrap-components=1.0.0 plotlydash-tornado-cmd=0.0.6
```
Install deps for support plotly + ipykernel
```
. /opt/conda/etc/profile.d/conda.sh && conda activate home/shared-v2/custom-kernels/conda-envs/<CONDA_ENV_NAME> && sudo /home/shared-v2/custom-kernels/conda-envs/<CONDA_ENV_NAME>/bin/pip install ipykernel jupyter-dash jupyter-server-proxy
```

Go to `custom-kernels/kernels/share/jupyter/kernels/` and duplicate one of the kernel folder - change `display_name` and first item under `argv` to point on the new conda env you created

## Clone boilerplate

open terminal and run:
```
git clone https://github.com/DreamTeamMember/dash_boilerplate.git ./<NAME_OF_APP_FOLDER>
```

## Preview
`plotly-preview-exmp.ipynb` is an example of a preview plotly app on jupyter.
1. Change cell 8 before running to fit your env name (`guy%20serfaty` is mine
2. Run all celld from top to bottom
3. After running the last cell you will see `Dash app running on https://jupyter-dev.playstudios-il.com/user/guy%20serfaty/proxy/8050/` - please open that link
4. On every change please rerun the `run_server` cell (last one) - the preview tab will automatically reload 


## Deploy
1. Change `BASE_PATH` on file: `utils/basepath.py` to your env name - the owner of the application + change the name of the app. It should look like: '/user/<ENV_NAME>/dash-<APP_NAME>'
2. Create new app [here](https://jupyter-dev.playstudios-il.com/hub/dashboards)
3. Choose the same APP_NAME you define on the basepath file
4. Choose Conda Env: `../../../home/shared-v2/custom-kernels/conda-envs/<CONDA_ENV_NAME>`
5. Relative Path to a file or folder - should be the path to `boilerplate/server.py`
