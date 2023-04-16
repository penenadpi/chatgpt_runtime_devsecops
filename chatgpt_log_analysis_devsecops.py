import requests
import json
import time



API_KEY = "YOUR_KEY"
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

def analyze_log_record(context, log, model="gpt-3.5-turbo", temperature=0.1, max_tokens=None):
    messages = [ {"role": "system", "content": f"{context}"}, {"role": "user", "content": f"Classify {log}"}]

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    data = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }

    if max_tokens is not None:
        data["max_tokens"] = max_tokens

    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

start = time.time()
context=""	
#context="Label suspicious = (00:09.2	15.42	TCP  	10001_123	4589	EXT_SERVER	22	13	2843	1	.APRS.	0), Label normal = (17:17.0	87709.785	TCP  	EXT_SERVER	8082	OPENSTACK_NET	50807	17031	  52.5 M	1	.AP.S.	0), Label suspicious= (00:02.3	62.046	TCP  	10004_35	57382	EXT_SERVER	22	7	420	1	.APRSF	0), Label normal = (43:39.0	183418.493	TCP  	OPENSTACK_NET	60802	EXT_SERVER	8082	20751	   5.8 M	1	.AP...	0), Label normal = (01:41.0	0.041	TCP  	OPENSTACK_NET	49838	EXT_SERVER	8000	6	614	1	.AP.SF	0)"


context="Label suspicious = (00:09.2	15.42	TCP  	10001_123	4589	EXT_SERVER	22	13	2843	1	.APRS.	0), Label normal = (17:17.0	87709.785	TCP  	EXT_SERVER	8082	OPENSTACK_NET	50807	17031	  52.5 M	1	.AP.S.	0), Label suspicious= (00:02.3	62.046	TCP  	10004_35	57382	EXT_SERVER	22	7	420	1	.APRSF	0), Label normal = (43:39.0	183418.493	TCP  	OPENSTACK_NET	60802	EXT_SERVER	8082	20751	   5.8 M	1	.AP...	0), Label suspicious = (48:21.0	121.48	TCP  	10004_35	32906	EXT_SERVER	22	5	291	1	.APRS.	0), Label normal = (47:48.7	0.072	TCP  	OPENSTACK_NET	63693	EXT_SERVER	8000	6	586	1	.AP.SF	0), Label normal = (46:39.5	0.049	TCP  	EXT_SERVER	8000	OPENSTACK_NET	50609	7	702	1	.AP.SF	0), Label suspicious = (58:55.7	0.027	TCP  	EXT_SERVER	3394	10081_11	59432	1	40	1	.A.R..	0	suspicious), Label suspicious = (59:42.9	8.645	TCP  	EXT_SERVER	22	10012_224	38807	19	3185	1	.AP.SF	0)"

log="08:49.7	0.046	TCP  	OPENSTACK_NET	63007	EXT_SERVER	8000	6	614	1	.AP.SF	0"

response_text = analyze_log_record(context, log)
end = time.time()
print(end-start)
print(response_text)
