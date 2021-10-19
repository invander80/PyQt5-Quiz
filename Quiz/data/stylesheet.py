class StyleSheets:
    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        self.scoreRight = """ QPushButton {
                                            background-color:#1e2124;
                                            border-radius:10px;
                                            border: 2px solid lime;
                                            color:#d9ecff;
                                            font: 700 9pt "Unispace";
                                            }
                                            """

        self.scoreWrong = """ QPushButton {
                                            background-color:#1e2124;
                                            border-radius:10px;
                                            border: 2px solid red;
                                            color:#d9ecff;
                	                        font: 700 9pt "Unispace";
                                            }
                                            """

        self.setStyleDefault = """ QPushButton {
                                            background-color:#303338;
                                            border-radius:10px;
                                            border: 2px solid #1e2124;
                                            color:#d9ecff;
                                            font: 700 9pt "Unispace";
                                            }
                                            QPushButton:hover {
                                            background-color: #393e45;
                                            }
                                            QPushButton:pressed {
        	                                background-color: #1e2124;
        	                                border: 2px solid #d9ecff;
                                            }
                                            """