# df: colunas id, date, NDVI, NDMI, R_SWIR...
g = df.groupby(["id","date"])
spatial = (g["NDVI"].agg(["mean","std","median"])
            .assign(cv_ndvi=lambda x: x["std"]/(x["mean"]+1e-9))
            .reset_index())
# Agrega por id (média/percentil do cv ao longo de datas)
cv_id = spatial.groupby("id")["cv_ndvi"].median().rename("cv_ndvi_med")
df = df.merge(cv_id, on="id", how="left")

df["date"] = pd.to_datetime(df["date"])
def duty_corridor(g):
    return ((g["NDVI"].between(0.45,0.70)) & (g["NDMI"].between(0.0,0.30))).mean()

def peaks_count(s, min_prom=0.05):
    import numpy as np
    x = s.to_numpy()
    # pico simples: vizinho menor dos dois lados + proeminência mínima
    cnt = 0
    for i in range(1,len(x)-1):
        if x[i]>x[i-1] and x[i]>x[i+1] and (x[i]-min(x[i-1],x[i+1])>=min_prom):
            cnt += 1
    return cnt

agg = (df.sort_values("date").groupby("id")
        .agg(NDVI_std=("NDVI","std"),
            NDVI_p95=("NDVI", lambda s: np.nanpercentile(s,95)),
            NDVI_p05=("NDVI", lambda s: np.nanpercentile(s,5)),
            duty=("NDVI", lambda s: duty_corridor(df.loc[s.index])),
            peaks=("NDVI", lambda s: peaks_count(s)))
        .reset_index())
agg["NDVI_range"] = agg["NDVI_p95"] - agg["NDVI_p05"]
df = df.merge(agg[["id","NDVI_std","NDVI_range","duty","peaks"]], on="id", how="left")

eps=1e-9
df["Slope_RE"]=(df["B6"]-df["B5"])/(740-705)
df["Curv_RE"]=df["B6"]-2*df["B5"]+df["B4"]
df["CIre"]= (df["B8"]/(df["B5"]+eps)) - 1
df["REP"]= 700 + 40 * (((df["B4"]+df["B7"])/2 - df["B5"]) / ((df["B6"]-df["B5"])+eps))

score_pasto =
w1*(1 - z(NDVI_std)) +
w2*(1 - z(NDVI_range)) +
w3*(z(duty)) +
w4*(1 - z(cv_ndvi_med)) +
w5*(1 - z(|Curv_RE - Curv_mid|)) +
w6*(1 - z(distância-a-protótipo-SAM))