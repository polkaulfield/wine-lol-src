# $Id: user.spec,v 1.3 1993/07/04 04:04:21 root Exp root $
#
name	user
id	2
length	540

1   pascal MessageBox(word ptr ptr word) MessageBox(1 2 3 4)
5   pascal InitApp(word) USER_InitApp(1)
6   pascal PostQuitMessage(word) PostQuitMessage(1)
33  pascal GetClientRect(word ptr) GetClientRect(1 2)
39  pascal BeginPaint(word ptr) BeginPaint(1 2)
40  pascal EndPaint(word ptr) EndPaint(1 2)
41  pascal CreateWindow(ptr ptr long word word word word word word word ptr) 
	   CreateWindow(1 2 3 4 5 6 7 8 9 10 11)
42  pascal ShowWindow(word word) ShowWindow(1 2)
57  pascal RegisterClass(ptr) RegisterClass(1)
66  pascal GetDC(word) GetDC(1)
85  pascal DrawText(word ptr word ptr word) DrawText(1 2 3 4 5)
104 pascal MessageBeep(word) MessageBeep(1)
107 pascal DefWindowProc(word word word long) DefWindowProc(1 2 3 4)
108 pascal GetMessage(ptr word word word) GetMessage(1 2 3 4)
113 pascal TranslateMessage(ptr) TranslateMessage(1)
114 pascal DispatchMessage(ptr) DispatchMessage(1)
124 pascal UpdateWindow(word) UpdateWindow(1)
151 pascal CreateMenu() CreateMenu()
157 pascal GetMenu(word) GetMenu(1)
158 pascal SetMenu(word word) SetMenu(1 2)
173 pascal LoadCursor(word ptr) RSC_LoadCursor(1 2)
174 pascal LoadIcon(word ptr) RSC_LoadIcon(1 2)
175 pascal LoadBitmap(word ptr) RSC_LoadBitmap(1 2)
176 pascal LoadString(word word ptr s_word) RSC_LoadString(1 2 3 4)
411 pascal AppendMenu(word word word ptr) AppendMenu(1 2 3 4)
