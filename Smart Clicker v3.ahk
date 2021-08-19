;Written By: Hellbent aka CivReborn
;Date Written: July 13th, 2017
;Date of Last Edit:July 19th, 2017
;Last PasteBin Save:
;Youtube Channel: https://www.youtube.com/user/CivReborn
#SingleInstance,Force
CoordMode, Mouse, Screen
SetMouseDelay,-1
Click_Delay := 0
Total_Clicks := 0
Stop := 0
Target_Window:=null
Gui,1:+AlwaysOnTop 
Gui,1:Color,White,Black
Gui,1:Add,GroupBox,x10 y10 w480 h50,Mode
Gui,1:Add,Radio, x130 y30 Group Checked vRad1 gClick_Mode ,Fixed
Gui,1:Add,Radio, x+100 y30  vRad2 gClick_Mode ,Free
Gui,1:Add,Button,x440 y27 w20 h20 gMy_Channel,?
Gui,1:Add,GroupBox, x10 y70 w480 h100,Target Window
Gui,1:Add,CheckBox, x30 y95 Checked vUse_Target_Window gSubmit_All,Use Target Window
Gui,1:Add,Button, x180 y85 w280 h30 gSet_Target_Window,Set Target Window
Gui,1:Add,Text,x30 y140 ,Target Window:
Gui,1:Add,Edit,cWhite x+20 w330 Center vTarget_Window
Gui,1:Add,GroupBox,x10 y180 w480 h100, Set Click Area/Target
Gui,1:Add,Button, x100 y210 w150 h30 vSet_Click_Target gSet_Fixed_Location,Set Click Target
Gui,1:Add,Edit,cWhite x+30 y215 w150 Center vTarget_Spot , 
Gui,1:Add,Text,x30 y250 vFixed_Text1,Box Width:
Gui,1:Add,Edit,cWhite x+20 w100 Center vBox_Width gSubmit_All,40
Gui,1:Add,Text,x+50 vFixed_Text2,Box Height:
Gui,1:Add,Edit,cWhite x+20 w100 Center vBox_Height gSubmit_All,40
Gui,1:Add,Button,x70 y200 w200 h30 Hidden vSet_Top_Left gSet_Top_Left,Set Top Left
Gui,1:Add,Edit,cWhite x+20 w150 y205 Center Hidden vTop_Left
Gui,1:Add,Button,x70 y240 w200 h30 Hidden vSet_Bottom_Right gSet_Bottom_Right,Set Bottom Right
Gui,1:Add,Edit,cWhite x+20 w150 y245 Center Hidden vBottom_Right
Gui,1:Add,GroupBox,x10 w480 h100,Speed && Display Options
Gui,1:Add,Checkbox,x30 y+-75 Checked vUse_Click_Delay gSubmit_All,Use Click Delay
Gui,1:Add,CheckBox,x+150 Checked vDisplay_Clicks gSubmit_All,Display Clicks
Gui,1:Add,Text,x30 yp+25,Delay:
Gui,1:Add,Edit,cWhite x+10  w100 Center vClick_Delay gSubmit_All,% Click_Delay
Gui,1:Add,Text,x+30 ,Total Clicks:
Gui,1:Add,Edit,cWhite x+10 w100 Center vTotal_Clicks,% Total_Clicks
Gui,1:Add,Button,x+10 w100 gReset_Click_Counter,Reset Click Count
Gui,1:Add,GroupBox,x10 w480 h55
Gui,1:Add,Button,x25 yp+15 w130 h30 gStart_Clicker,Start
Gui,1:Add,Button,x+30  w130 h30 gStop_Clicker,Stop
Gui,1:Add,Button,x+30  w130 h30 gReset,Reset
Gui,1:Show,,Smart Clicker v3.0
Gui,1:Submit,NoHide
return
GuiClose:
	ExitApp	
Submit_All:
	Gui,1:Submit,NoHide
	return
My_Channel:
	Run, https://www.youtube.com/user/CivReborn
	return
Reset:
	Reload
Reset_Click_Counter:
	Total_Clicks := 0
	GuiControl,1:,Total_Clicks,% Total_Clicks
	return
Click_Mode:
	Gui,1:Submit,NoHide
	if(Rad1==1)
		{
			GuiControl,1:Show,Set_Click_Target
			GuiControl,1:Show,Target_Spot
			GuiControl,1:Show,Fixed_Text1
			GuiControl,1:Show,Fixed_Text2
			GuiControl,1:Show,Box_Width
			GuiControl,1:Show,Box_Height
			GuiControl,1:Hide,Set_Top_Left
			GuiControl,1:Hide,Set_Bottom_Right
			GuiControl,1:Hide,Top_Left
			GuiControl,1:Hide,Bottom_Right
		}
	else if(Rad2==1)
		{
			GuiControl,1:Show,Set_Top_Left
			GuiControl,1:Show,Set_Bottom_Right
			GuiControl,1:Show,Top_Left
			GuiControl,1:Show,Bottom_Right
			GuiControl,1:Hide,Set_Click_Target
			GuiControl,1:Hide,Target_Spot
			GuiControl,1:Hide,Fixed_Text1
			GuiControl,1:Hide,Fixed_Text2
			GuiControl,1:Hide,Box_Width
			GuiControl,1:Hide,Box_Height
		}
	return
Set_Target_Window:
	isPressed:=0
	i:= 0
	Loop
		{
			Left_Mouse:=GetKeyState("LButton")
			WinGetTitle,Temp_Window,A
			ToolTip,Left Click on the target window twice to set `n`n Current Window: %Temp_Window%
			if(Left_Mouse==False&&isPressed==0)
				isPressed:=1
			else if(Left_Mouse==True&&isPressed==1)
				{
					i++
					isPressed:=0
					if(i>=2)
						{
							WinGetTitle,Target_Window,A
							ToolTip,
							break
						}
				}
		}
	GuiControl,1:,Target_Window,% Target_Window	
	return
Set_Fixed_Location:
	Stop:=1
	Get_Click_Pos(Fixed_X,Fixed_Y)	
	GuiControl,1:,Target_Spot,X = %Fixed_X%    Y = %Fixed_Y%		
	return	
Set_Top_Left:
	Stop:=1
	Get_Click_Pos(Top_Left_X,Top_Left_Y)		
	GuiControl,1:,Top_Left,X = %Top_Left_X%    Y = %Top_Left_Y%	
	return
Set_Bottom_Right:
	Stop:=1
	Get_Click_Pos(Bottom_Right_X,Bottom_Right_Y)	
	GuiControl,1:,Bottom_Right,X = %Bottom_Right_X%    Y = %Bottom_Right_Y%	
	return
Start_Clicker:
	Stop:=0
	if(Rad1==1)
		{
			Run_Fixed(Fixed_X,Fixed_Y)
		}
	else if(Rad2==1)
		{
			Run_Free()
		}
	return
Stop_Clicker:
	Stop:=1
	return	
Run_Fixed(ByRef Fixed_X,ByRef Fixed_Y)
	{
		global
		Size_W:=Box_Width//2
		Size_H:=Box_Height//2
		
		if(Fixed_X!=null&&Fixed_Y!=null)
			{
				if(Use_Target_Window==1)
					{
						if(Target_Window==null)
							{
								MsgBox, 262192, Missing Info,You need to set your target window!
								return
							}
						if(Use_Click_Delay==1&&Display_Clicks==1)
							{
								Loop	
									{
										if(Stop==1)
											{
												break
											}
										WinGetTitle,Active_Window,A
										MouseGetPos,temp_X,temp_Y
										if(Active_Window==Target_Window&&temp_X>=(Fixed_X-Size_W)&&temp_X<=(Fixed_X+Size_W)&&temp_Y>=(Fixed_Y-Size_H)&&temp_Y<=(Fixed_Y+Size_H))
											{
												Click, %Fixed_X%  %Fixed_Y%
												Total_Clicks++
												GuiControl,1:,Total_Clicks,% Total_Clicks
												Sleep, %Click_Delay%
											}
									}
							}
						else if(Use_Click_Delay==1&&Display_Clicks==0)
							{
								Loop	
									{
										if(Stop==1)
											{
												break
											}
										WinGetTitle,Active_Window,A
										MouseGetPos,temp_X,temp_Y
										if(Active_Window==Target_Window&&temp_X>=(Fixed_X-Size_W)&&temp_X<=(Fixed_X+Size_W)&&temp_Y>=(Fixed_Y-Size_H)&&temp_Y<=(Fixed_Y+Size_H))
											{
												Click, %Fixed_X%  %Fixed_Y%
												Sleep, %Click_Delay%
											}
									}
							}
						else if(Use_Click_Delay==0&&Display_Clicks==1)
							{
								Loop	
									{
										if(Stop==1)
											{
												break
											}
										WinGetTitle,Active_Window,A
										MouseGetPos,temp_X,temp_Y
										if(Active_Window==Target_Window&&temp_X>=(Fixed_X-Size_W)&&temp_X<=(Fixed_X+Size_W)&&temp_Y>=(Fixed_Y-Size_H)&&temp_Y<=(Fixed_Y+Size_H))
											{
												Click, %Fixed_X%  %Fixed_Y%
												Total_Clicks++
												GuiControl,1:,Total_Clicks,% Total_Clicks
											}
									}
							}
						else if(Use_Click_Delay==0&&Display_Clicks==0)
							{
								Loop	
									{
										if(Stop==1)
											{
												break
											}
										WinGetTitle,Active_Window,A
										MouseGetPos,temp_X,temp_Y
										if(Active_Window==Target_Window&&temp_X>=(Fixed_X-Size_W)&&temp_X<=(Fixed_X+Size_W)&&temp_Y>=(Fixed_Y-Size_H)&&temp_Y<=(Fixed_Y+Size_H))
											{
												Click, %Fixed_X%  %Fixed_Y%
											}
									}
							}	
					}
				else if(Use_Target_Window==0)
					{
						if(Use_Click_Delay==1&&Display_Clicks==1)
							{
								Loop	
									{
										if(Stop==1)
											{
												break
											}
										MouseGetPos,temp_X,temp_Y
										if(temp_X>=(Fixed_X-Size_W)&&temp_X<=(Fixed_X+Size_W)&&temp_Y>=(Fixed_Y-Size_H)&&temp_Y<=(Fixed_Y+Size_H))
											{
												Click, %Fixed_X%  %Fixed_Y%
												Total_Clicks++
												GuiControl,1:,Total_Clicks,% Total_Clicks
												Sleep, %Click_Delay%
											}
									}
							}
						else if(Use_Click_Delay==1&&Display_Clicks==0)
							{
								Loop	
									{
										if(Stop==1)
											{
												break
											}
										MouseGetPos,temp_X,temp_Y
										if(temp_X>=(Fixed_X-Size_W)&&temp_X<=(Fixed_X+Size_W)&&temp_Y>=(Fixed_Y-Size_H)&&temp_Y<=(Fixed_Y+Size_H))
											{
												Click, %Fixed_X%  %Fixed_Y%
												Sleep, %Click_Delay%
											}
									}
							}
						else if(Use_Click_Delay==0&&Display_Clicks==1)
							{
								Loop	
									{
										if(Stop==1)
											{
												break
											}
										MouseGetPos,temp_X,temp_Y
										if(temp_X>=(Fixed_X-Size_W)&&temp_X<=(Fixed_X+Size_W)&&temp_Y>=(Fixed_Y-Size_H)&&temp_Y<=(Fixed_Y+Size_H))
											{
												Click, %Fixed_X%  %Fixed_Y%
												Total_Clicks++
												GuiControl,1:,Total_Clicks,% Total_Clicks
											}
									}
							}
						else if(Use_Click_Delay==0&&Display_Clicks==0)
							{
								Loop	
									{
										if(Stop==1)
											{
												break
											}
										MouseGetPos,temp_X,temp_Y
										if(temp_X>=(Fixed_X-Size_W)&&temp_X<=(Fixed_X+Size_W)&&temp_Y>=(Fixed_Y-Size_H)&&temp_Y<=(Fixed_Y+Size_H))
											{
												Click, %Fixed_X%  %Fixed_Y%
											}
									}
							}	
					}
			}
		else if(Fixed_X==null)
			{
				MsgBox, 262192, Missing Info,You need to set your Click Location!
			}
	}
Run_Free()
	{
		global
		if(Top_Left_X!=null&&Bottom_Right_X!=null)
			{
				if(Use_Target_Window==1)
					{
						if(Target_Window==null)
							{
								MsgBox, 262192, Missing Info,You need to set your target window!
								return
							}
						if(Use_Click_Delay==1&&Display_Clicks==1)
							{
								Loop	
									{
										if(Stop==1)
											{
												break
											}
										WinGetTitle,Active_Window,A
										MouseGetPos,temp_X,temp_Y
										if(Active_Window==Target_Window&&temp_X>=Top_Left_X&&temp_X<=Bottom_Right_X&&temp_Y>=Top_Left_Y&&temp_Y<=Bottom_Right_Y)
											{
												Click, %Temp_X%  %Temp_Y%
												Total_Clicks++
												GuiControl,1:,Total_Clicks,% Total_Clicks
												Sleep, %Click_Delay%
											}
									}
							}	
						else if(Use_Click_Delay==1&&Display_Clicks==0)
							{
								Loop	
									{
										if(Stop==1)
											{
												break
											}
										WinGetTitle,Active_Window,A
										MouseGetPos,temp_X,temp_Y
										if(Active_Window==Target_Window&&temp_X>=Top_Left_X&&temp_X<=Bottom_Right_X&&temp_Y>=Top_Left_Y&&temp_Y<=Bottom_Right_Y)
											{
												Click, %Temp_X%  %Temp_Y%
												Sleep, %Click_Delay%
											}
									}
							}
						else if(Use_Click_Delay==0&&Display_Clicks==0)
							{
								Loop	
									{
										if(Stop==1)
											{
												break
											}
										WinGetTitle,Active_Window,A
										MouseGetPos,temp_X,temp_Y
										if(Active_Window==Target_Window&&temp_X>=Top_Left_X&&temp_X<=Bottom_Right_X&&temp_Y>=Top_Left_Y&&temp_Y<=Bottom_Right_Y)
											{
												Click, %Temp_X%  %Temp_Y%
											}
									}
							}	
						if(Use_Click_Delay==0&&Display_Clicks==1)
							{
								Loop	
									{
										if(Stop==1)
											{
												break
											}
										WinGetTitle,Active_Window,A
										MouseGetPos,temp_X,temp_Y
										if(Active_Window==Target_Window&&temp_X>=Top_Left_X&&temp_X<=Bottom_Right_X&&temp_Y>=Top_Left_Y&&temp_Y<=Bottom_Right_Y)
											{
												Click, %Temp_X%  %Temp_Y%
												Total_Clicks++
												GuiControl,1:,Total_Clicks,% Total_Clicks
											}
									}
							}		
					}
				else if(Use_Target_Window==0)
					{
						if(Use_Click_Delay==1&&Display_Clicks==1)
							{
								Loop	
									{
										if(Stop==1)
											{
												break
											}
										MouseGetPos,temp_X,temp_Y
										if(temp_X>=Top_Left_X&&temp_X<=Bottom_Right_X&&temp_Y>=Top_Left_Y&&temp_Y<=Bottom_Right_Y)
											{
												Click, %Temp_X%  %Temp_Y%
												Total_Clicks++
												GuiControl,1:,Total_Clicks,% Total_Clicks
												Sleep, %Click_Delay%
											}
									}
							}	
						else if(Use_Click_Delay==1&&Display_Clicks==0)
							{
								Loop	
									{
										if(Stop==1)
											{
												break
											}
										MouseGetPos,temp_X,temp_Y
										if(temp_X>=Top_Left_X&&temp_X<=Bottom_Right_X&&temp_Y>=Top_Left_Y&&temp_Y<=Bottom_Right_Y)
											{
												Click, %Temp_X%  %Temp_Y%
												Sleep, %Click_Delay%
											}
									}
							}
						else if(Use_Click_Delay==0&&Display_Clicks==0)
							{
								Loop	
									{
										if(Stop==1)
											{
												break
											}
										MouseGetPos,temp_X,temp_Y
										if(temp_X>=Top_Left_X&&temp_X<=Bottom_Right_X&&temp_Y>=Top_Left_Y&&temp_Y<=Bottom_Right_Y)
											{
												Click, %Temp_X%  %Temp_Y%
											}
									}
							}	
						if(Use_Click_Delay==0&&Display_Clicks==1)
							{
								Loop	
									{
										if(Stop==1)
											{
												break
											}
										MouseGetPos,temp_X,temp_Y
										if(temp_X>=Top_Left_X&&temp_X<=Bottom_Right_X&&temp_Y>=Top_Left_Y&&temp_Y<=Bottom_Right_Y)
											{
												Click, %Temp_X%  %Temp_Y%
												Total_Clicks++
												GuiControl,1:,Total_Clicks,% Total_Clicks
											}
									}
							}		
					}
			}
		else
			MsgBox, 262192, Missing Info,You need to set your Top Left And Bottom Right Click Location!			
	}
Get_Click_Pos(ByRef X,ByRef Y)
	{
		isPressed:=0
		i:=0
		Loop
			{
				Left_Mouse:=GetKeyState("LButton")
				MouseGetPos,X,Y,
				ToolTip,Left Click Your Target Location To Set It  `n`nCurrent Location: `nX = %X%`nY = %Y% 
				if(Left_Mouse==False&&isPressed==0)
					isPressed:=1
				else if(Left_Mouse==True&&isPressed==1)
					{
						MouseGetPos,X,Y,
						ToolTip,
						break
					}
			}
	}
esc::ExitApp