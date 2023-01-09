import tkinter as tk
import tkintermapview
import mpu

class MapFrameClass:

    def buildFrame(self, fatherFrame):
        self.fatherFrame = fatherFrame
        self.MapFrame = tk.Frame(fatherFrame)
        self.startingNewWP = False

        self.planning = False
        self.count = 0
        self.positions = []
        self.markers = []

        self.button1 = tk.Button(self.MapFrame, width=10, text="Start", bg='green', fg="white", command=self.start)
        self.button1.grid(row=0, column=0, padx=5, pady=5)
        self.button2 = tk.Button(self.MapFrame, width=10, text="Finish", bg='red', fg="white", command=self.finish)
        self.button2.grid(row=0, column=1, padx=5, pady=5)
        self.button3 = tk.Button(self.MapFrame, width=10, text="Clear", bg='blue', fg="white", command=self.clear)
        self.button3.grid(row=0, column=2, padx=5, pady=5)

        self.map_widget = tkintermapview.TkinterMapView(self.MapFrame, width=800, height=600, corner_radius=0)
        self.map_widget.grid(row=1, column=0, columnspan = 2, padx=5, pady=5)
        self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga",
                                        max_zoom=22)
        self.map_widget.set_position(41.275946, 1.987475)
        self.map_widget.set_zoom(20)

        self.map_widget.add_right_click_menu_command(label="Insert WP", command=self.add_marker_event,pass_coords=True)


        return self.MapFrame

    def add_marker_event(self, position):
        if self.planning:
            self.count = self.count + 1
            marker = self.map_widget.set_marker(position[0], position[1], text=self.count)
            self.startingNewWP = True

            if self.count > 1:
                path = self.map_widget.set_path([self.positions[-1], position], color='red')
                self.paths.append(path)

            self.positions.append(position)
            self.markers.append(marker)

    def start(self):
        self.planning = True
        self.count = 0
        self.positions = []
        self.markers = []
        self.paths = []
        self.currentPath = None
        self.coords = []
        self.map_widget.canvas.bind("<Motion>", self.drag)

    def finish(self):
        self.planning = False
        path = self.map_widget.set_path(self.positions, color='green')
        self.paths.append(path)
        if self.currentPath:
            self.currentPath.delete()
        self.map_widget.canvas.unbind("<Motion>")


    def clear(self):
        self.count = 0
        self.positions = []
        for marker in self.markers:
            marker.delete()
        self.markers = []
        for path in self.paths:
            path.delete()
        self.paths = []

    def drag(self, e):
        if self.startingNewWP:
            self.coords.append(e)
            self.startingNewWP = False
            self.distance = self.map_widget.canvas.create_text(e.x, e.y, text='0', font=("Courier", 15, 'bold'), fill='blue', tags="distance")
        p = self.map_widget.convert_canvas_coords_to_decimal_coords(e.x, e.y)
        if self.count > 0:
            if self.currentPath:
                self.currentPath.delete()
            self.currentPath = self.map_widget.set_path([self.positions[-1], p], color='red')
            dist = mpu.haversine_distance(self.positions[-1], p) * 1000
            midPoint = ((self.coords[-1].x + e.x) // 2, (self.coords[-1].y + e.y) // 2)
            self.map_widget.canvas.coords(self.distance, midPoint)
            self.map_widget.canvas.itemconfig(self.distance, text=str(round(dist, 2)) + 'm')
