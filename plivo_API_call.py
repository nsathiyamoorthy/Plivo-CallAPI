import plivo,time

client = plivo.RestClient(auth_id='MANJCWMZNJZJJKMZKYNJ', auth_token='ODJkZjM2YjE1ODVkODYyZjRiMjFjM2VhMDE4Yzk3')
#client = plivo.RestClient()
caller='16469165329'
callee='sip:plasnmtep23023997139802448463876@phone.plivo.com:5060'
a_url='https://s3.amazonaws.com/plivosamplexml/play_url.xml'
caler="Sathiya playing music"
a_mtd='GET'
j=0

cll = client.calls.create( from_=caller, to_=callee, answer_url=a_url, answer_method=a_mtd, caller_name=caler, )

print("\nPlease Wait for few seconds",callee,"is being called by Plivo\n")

#Following While Loop is to wait till live calls API to return proper Call_UUID
while client.live_calls.list_ids().calls == []:
        j+=1
#acal=time.time()
#print("\n",j, acal-bcal,"\n" ) this value is RTT and found to be 2.5 sec

#Live Calls list
clls=client.live_calls.list_ids()
#extracting the call as there was only oe live call
ciid=clls.calls[0]
#Call Detail
cdl=client.live_calls.get(ciid)

print(cdl)
cl=client.live_calls.get(ciid)

if cl.call_uuid == cll.request_uuid:
        print("\nCall created by Plivo and call is ",cl.call_status,"state.\n\n Live calls api returned the Call_UUID",clls.calls[0], "\n \"request_uuid\" returned by Call api ", cll.request_uuid)
j=2

while client.live_calls.list_ids().calls != [] and j >= 0:
    if cl.call_uuid == cll.request_uuid and cl.call_status in ['in-progress', 'ringing']:
        j-=1
        cl=client.live_calls.get(ciid)
        print("\nCall created by Plivo and call is ",cl.call_status,"state and UUID is", ciid)

    else:
        print("This API test fails check the above prints and this python file")
        exit(0)

print('\n Call is being terminated by the Plivo API\n\n Call Details as below')
client.calls.delete(ciid)

#if client.calls.get(ciid).call_uuid == ciid:
while True: 
    try:
        cdr=client.calls.get(ciid)
        break
    except:
        print("\n Waiting to get the CDR")
        continue

print(cdr)

