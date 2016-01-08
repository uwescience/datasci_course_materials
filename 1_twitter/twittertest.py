from twitter import Twitter, OAuth

api_key = "ZJTpB1RVFzB26MgDgEpkvYEcV"
api_secret = "EoWW9qZxsjNCimCDLGOlZicXKkUoV15CmXZuP9XuIpogq74xBd"
access_token_key = "18296585-qqkTCTFaRCamQKQMEDu2J0wQv6usnUUOmSJNiy4Tz"
access_token_secret = "iURdN3MmI5OZUnlIPm2Jz7iamL8D4dKiMib2aC8zg4sPk"

t = Twitter(auth=OAuth(access_token_key, access_token_secret, api_key, api_secret))

response = t.search.tweets(q="#coursera")
response["statuses"][:20]
