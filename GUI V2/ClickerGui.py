import pygame
class ClickerGui:
	WINDOW_WIDTH = 150
	WINDOW_HEIGHT = 125
	DROPDOWN_HEIGHT = 100
	def __init__(self):
		self.LIGHT_GRAY = pygame.Color(60, 70, 73)
		self.DARK_GRAY = pygame.Color(45, 47, 49)
		self.GREEN = pygame.Color(35, 168, 105)

		self.frame = new JFrame("7Clicker")

		self.mainPane = JPanel(null)
		self.titleBar = JPanel(null)
		self.dropdown = JPanel(null)

		self.titleText = JLabel("7Clicker")
		self.cpsRange = JLabel("CPS Range")
		self.cpsNumber = JLabel("00")
		self.dropdownArrow = pygame.image.load("assets/arrow_down.png")
		self.powerButton = pygame.image.load("assets/power_button.png")
		self.toggleKeyText = JLabel("Toggle Button")

		self.minCPSField = JTextField("8", 2)
		self.maxCPSField = JTextField("12", 2)
		self.toggleKeyField =  JTextField("Mouse 3")

		self.overlayBox =  JCheckBox("Overlay", True)
		self.rightClickBox =  JCheckBox("Right Click", False)

		self.slider =  RangeSlider(mainPane, 10, 130)

		self.focused = False

	public ClickerGui() {
		setupFrame()
		setupMainPane()
		setupTitleBar()
		setupDropdown()
		setupSettings()
		setupMisc()
	}

	private void setupFrame() {
		frame.setSize(WINDOW_WIDTH, WINDOW_HEIGHT)
		frame.setLocation(50, 50)
		frame.setLayout(null)
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
		frame.setUndecorated(True)
		frame.setBackground(Color(0, 0, 0, 0))
		frame.setAlwaysOnTop(True)
		frame.setResizable(False)

		if (System.getProperty("os.name").toLowerCase().contains("mac")) {
			Application.getApplication().setDockIconImage(
					 ImageIcon(AutoClicker.class.getClassLoader().getResource("assets/7Clicker.png")).getImage())
		} else {
			frame.setIconImage(
					 ImageIcon(AutoClicker.class.getClassLoader().getResource("assets/7Clicker.png")).getImage())
		}

		frame.addWindowFocusListener( WindowAdapter() {
			@Override
			public void windowGainedFocus(WindowEvent e) {
				frame.requestFocusInWindow()
				focused = True
			}

			@Override
			public void windowLostFocus(WindowEvent e) {
				frame.requestFocusInWindow()
				focused = False
			}
		})

		Toolkit.getDefaultToolkit().addAWTEventListener( AWTEventListener() {
			public void eventDispatched(AWTEvent event) {
				if (event.getID() == MouseEvent.MOUSE_CLICKED) {
					if (!(((MouseEvent) event).getSource() instanceof JTextField)) {
						KeyboardFocusManager.getCurrentKeyboardFocusManager().clearGlobalFocusOwner()
					}
				}
			}
		}, AWTEvent.MOUSE_EVENT_MASK)
	}

	private void setupMainPane() {
		mainPane.setBounds(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT + DROPDOWN_HEIGHT)
		mainPane.setBackground(LIGHT_GRAY)
		mainPane.setBorder(BorderFactory.createMatteBorder(5, 5, 5, 5, DARK_GRAY))

		powerButton.setBounds(10, 45, 50, 50)

		powerButton.addMouseListener(new MouseAdapter() {
			@Override
			public void mousePressed(MouseEvent e) {
				AutoClicker.toggle()
			}
		})

		mainPane.add(powerButton)
		cpsNumber.setBounds(75, 45, 75, 50)
		cpsNumber.setForeground(GREEN)
		mainPane.add(cpsNumber)
	}

	private void setupTitleBar() {
		MouseAdapter dragListener = new MouseAdapter() {
			private int pX, pY

			@Override
			public void mousePressed(MouseEvent e) {
				pX = e.getX()
				pY = e.getY()
			}

			@Override
			public void mouseDragged(MouseEvent e) {
				frame.setLocation(frame.getLocation().x + e.getX() - pX, frame.getLocation().y + e.getY() - pY)
			}
		}

		titleBar.setBounds(0, 0, WINDOW_WIDTH, 30)
		titleBar.setBackground(DARK_GRAY)
		titleBar.addMouseListener(dragListener)
		titleBar.addMouseMotionListener(dragListener)

		titleText.setBounds(0, 0, WINDOW_WIDTH, 30)
		titleText.setHorizontalAlignment(SwingConstants.CENTER)
		titleText.setForeground(Color.WHITE)
		titleBar.add(titleText)
	}

	private void setupDropdown() {
		dropdown.setBounds(0, WINDOW_HEIGHT - 15, WINDOW_WIDTH, 15)
		dropdown.setBackground(DARK_GRAY)

		dropdown.addMouseListener( MouseAdapter() {
			@Override
			public void mousePressed(MouseEvent e) {
				if (frame.getHeight() == WINDOW_HEIGHT) {
					dropdownArrow.setIcon(
							 ImageIcon(AutoClicker.class.getClassLoader().getResource("assets/arrow_up.png")))
					Timeline dropdownTimeline =  Timeline(dropdown)
					dropdownTimeline.addPropertyToInterpolate("location", dropdown.getLocation(),
							 Point(0, dropdown.getY() + DROPDOWN_HEIGHT))
					dropdownTimeline.setDuration(300)
					dropdownTimeline.play()

					Timeline frameTimeline = new Timeline(frame)
					frameTimeline.addPropertyToInterpolate("size", frame.getSize(),
							new Dimension(WINDOW_WIDTH, WINDOW_HEIGHT + DROPDOWN_HEIGHT))
					frameTimeline.setDuration(300)
					frameTimeline.play()

					KeyboardFocusManager.getCurrentKeyboardFocusManager().clearGlobalFocusOwner()
				} else if (frame.getHeight() == WINDOW_HEIGHT + DROPDOWN_HEIGHT) {
					dropdownArrow.setIcon(
							new ImageIcon(AutoClicker.class.getClassLoader().getResource("assets/arrow_down.png")))

					Timeline dropdownTimeline = new Timeline(dropdown)
					dropdownTimeline.addPropertyToInterpolate("location", dropdown.getLocation(),
							new Point(0, WINDOW_HEIGHT - 15))
					dropdownTimeline.setDuration(300)
					dropdownTimeline.play()

					Timeline frameTimeline = new Timeline(frame)
					frameTimeline.addPropertyToInterpolate("size", frame.getSize(),
							new Dimension(WINDOW_WIDTH, WINDOW_HEIGHT))
					frameTimeline.setInitialDelay(50)
					frameTimeline.setDuration(300)
					frameTimeline.play()

					KeyboardFocusManager.getCurrentKeyboardFocusManager().clearGlobalFocusOwner()
				}
			}
		})

		dropdownArrow.setBounds(69, 2, 13, 10)
		dropdown.add(dropdownArrow)
	}

	private void setupSettings() {
		cpsRange.setBounds(0, 110, WINDOW_WIDTH, 13)
		cpsRange.setHorizontalAlignment(SwingConstants.CENTER)
		cpsRange.setForeground(Color.WHITE)
		mainPane.add(cpsRange)

		minCPSField.setBounds(10, 140, 20, 20)
		minCPSField.setHorizontalAlignment(SwingConstants.CENTER)
		minCPSField.setBackground(DARK_GRAY)
		minCPSField.setForeground(Color.WHITE)
		minCPSField.setBorder(BorderFactory.createEmptyBorder(2, 2, 2, 2))

		minCPSField.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				textFieldSetCPS(True)
			}
		})

		minCPSField.addFocusListener(new FocusAdapter() {
			@Override
			public void focusLost(FocusEvent e) {
				textFieldSetCPS(True)
			}
		})

		mainPane.add(minCPSField)

		maxCPSField.setBounds(WINDOW_WIDTH - 30, 140, 20, 20)
		maxCPSField.setHorizontalAlignment(SwingConstants.CENTER)
		maxCPSField.setBackground(DARK_GRAY)
		maxCPSField.setForeground(Color.WHITE)
		maxCPSField.setBorder(BorderFactory.createEmptyBorder(2, 2, 2, 2))

		maxCPSField.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				textFieldSetCPS(False)
			}
		})

		maxCPSField.addFocusListener(new FocusAdapter() {
			@Override
			public void focusLost(FocusEvent e) {
				textFieldSetCPS(False)
			}
		})

		mainPane.add(maxCPSField)

		overlayBox.setBounds(5, 163, 67, 16)
		overlayBox.setBackground(LIGHT_GRAY)
		overlayBox.setForeground(Color.WHITE)
		overlayBox.setIcon(
				new ImageIcon(AutoClicker.class.getClassLoader().getResource("assets/checkbox_unchecked.png")))
		overlayBox.setSelectedIcon(
				new ImageIcon(AutoClicker.class.getClassLoader().getResource("assets/checkbox_checked.png")))

		overlayBox.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				frame.setAlwaysOnTop(overlayBox.isSelected())
			}
		})

		mainPane.add(overlayBox)

		rightClickBox.setBounds(66, 163, 80, 16)
		rightClickBox.setBackground(LIGHT_GRAY)
		rightClickBox.setForeground(Color.WHITE)
		rightClickBox.setIcon(
				new ImageIcon(AutoClicker.class.getClassLoader().getResource("assets/checkbox_unchecked.png")))
		rightClickBox.setSelectedIcon(
				new ImageIcon(AutoClicker.class.getClassLoader().getResource("assets/checkbox_checked.png")))

		rightClickBox.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				AutoClicker.button = (rightClickBox.isSelected()) ? 2 : 1
			}
		})

		mainPane.add(rightClickBox)

		toggleKeyText.setBounds(11, 180, 66, 25)
		toggleKeyText.setForeground(Color.WHITE)
		mainPane.add(toggleKeyText)

		toggleKeyField.setBounds(WINDOW_WIDTH - 70, 182, 60, 20)
		toggleKeyField.setHorizontalAlignment(SwingConstants.CENTER)
		toggleKeyField.setBackground(DARK_GRAY)
		toggleKeyField.setForeground(Color.WHITE)
		toggleKeyField.setBorder(BorderFactory.createEmptyBorder(2, 2, 2, 2))

		((AbstractDocument) toggleKeyField.getDocument()).setDocumentFilter(new DocumentFilter() {
			@Override
			public void replace(FilterBypass fb, int offset, int length, String text, AttributeSet attributes)
					throws BadLocationException {
				if (offset == -1 && length == -1) {
					super.replace(fb, 0, toggleKeyField.getText().length(), text, attributes)
				}
			}

			@Override
			public void remove(FilterBypass fb, int offset, int length) throws BadLocationException {
				// NO-OP
			}

			@Override
			public void insertString(FilterBypass fb, int offset, String string, AttributeSet attributes)
					throws BadLocationException {
				// NO-OP
			}
		})

		toggleKeyField.addKeyListener(new KeyAdapter() {
			@Override
			public void keyPressed(KeyEvent e) {
				try {
					if (!KeyEvent.getKeyModifiersText(e.getModifiers()).contains(KeyEvent.getKeyText(e.getKeyCode()))
							&& e.getKeyCode() != KeyEvent.VK_CAPS_LOCK) {
						AutoClicker.toggleKey[0] = KeyEvent.getKeyText(e.getKeyCode())
						AutoClicker.toggleKey[1] = KeyEvent.getKeyModifiersText(e.getModifiers())
						AutoClicker.toggleMouseButton = -1
						((AbstractDocument) toggleKeyField.getDocument()).replace(-1, -1,
								getKeyString(e.getKeyCode(), e.getModifiers()), null)
					}
				} catch (BadLocationException ex) {
					ex.printStackTrace()
				}
			}
		})

		toggleKeyField.addMouseListener(new MouseAdapter() {
			@Override
			public void mousePressed(MouseEvent e) {
				try {
					if (e.getButton() == 2 || e.getButton() > 3) {
						AutoClicker.toggleMouseButton = (e.getButton() == 2) ? 3 : e.getButton()
						AutoClicker.toggleKey[0] = ""
						AutoClicker.toggleKey[1] = ""
						((AbstractDocument) toggleKeyField.getDocument()).replace(-1, -1,
								"Mouse " + ((e.getButton() == 2) ? 3 : e.getButton()), null)
					}
				} catch (BadLocationException ex) {
					ex.printStackTrace()
				}
			}
		})

		mainPane.add(toggleKeyField)
	}

	private void setupMisc() {
		try {
			GraphicsEnvironment ge = GraphicsEnvironment.getLocalGraphicsEnvironment()
			InputStream fontFile = AutoClicker.class.getClassLoader().getResourceAsStream("assets/BebasNeue.otf")
			Font font = Font.createFont(Font.TrueTYPE_FONT, fontFile)
			ge.registerFont(font)
			fontFile.close()

			titleText.setFont(font.deriveFont(Font.PLAIN, 25))
			cpsNumber.setFont(font.deriveFont(Font.PLAIN, 69))
			cpsRange.setFont(font.deriveFont(Font.PLAIN, 18))
			overlayBox.setFont(font.deriveFont(Font.PLAIN, 14))
			rightClickBox.setFont(font.deriveFont(Font.PLAIN, 14))
			toggleKeyText.setFont(font.deriveFont(Font.PLAIN, 14))
			minCPSField.setFont(new Font("arial", Font.PLAIN, 12))
			maxCPSField.setFont(new Font("arial", Font.PLAIN, 12))
			toggleKeyField.setFont(new Font("arial", Font.PLAIN, 12))
		} catch (IOException | FontFormatException e) {
			e.printStackTrace()
		}

		frame.add(titleBar)
		frame.add(dropdown)
		frame.add(mainPane)
		frame.setVisible(True)
	}

	private void textFieldSetCPS(boolean isMin) {
		JTextField textField = isMin ? minCPSField : maxCPSField

		if (textField.getText().matches("^\\d+$")
				&& (isMin && Integer.parseInt(textField.getText()) >= 1
						&& Integer.parseInt(textField.getText()) <= AutoClicker.maxCPS)
				|| (!isMin && Integer.parseInt(textField.getText()) >= AutoClicker.minCPS
						&& Integer.parseInt(textField.getText()) <= 99)) {
			int cpsFieldVal = Integer.parseInt(textField.getText())

			if ((isMin && slider.sliderVal1 <= slider.sliderVal2)
					|| (!isMin && slider.sliderVal1 > slider.sliderVal2)) {
				slider.sliderVal1 = (cpsFieldVal > 20) ? 19 : cpsFieldVal - 1
				slider.sliderThumb1.x = (slider.sliderVal1 / 20.0f) * 130
			} else {
				slider.sliderVal2 = (cpsFieldVal > 20) ? 19 : cpsFieldVal - 1
				slider.sliderThumb2.x = (slider.sliderVal2 / 20.0f) * 130
			}

			slider.sliderRange.x = Math.min(slider.sliderThumb1.x, slider.sliderThumb2.x) + 5
			slider.sliderRange.width = Math.max(slider.sliderThumb1.x, slider.sliderThumb2.x)
					- Math.min(slider.sliderThumb1.x, slider.sliderThumb2.x)
			textField.setText(textField.getText().replaceFirst("^0*", ""))
			KeyboardFocusManager.getCurrentKeyboardFocusManager().clearGlobalFocusOwner()

			if (isMin) {
				AutoClicker.minCPS = cpsFieldVal
			} else {
				AutoClicker.maxCPS = cpsFieldVal
			}

			slider.repaint()
		} else {
			textField.setText(String.valueOf(isMin ? AutoClicker.minCPS : AutoClicker.maxCPS))
		}
	}

	private String getKeyString(int keyCode, int modifiers) {
		String modifiersString = KeyEvent.getKeyModifiersText(modifiers).replace("+", "")
		String keyString

		if (keyCode == 0) {
			keyString = "Invalid Key"
			modifiersString = ""
		} else if (keyCode == 32) {
			keyString = "Space"
		} else {
			keyString = KeyEvent.getKeyText(keyCode)
		}

		return modifiersString + keyString
	}
}