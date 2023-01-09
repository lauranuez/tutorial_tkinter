import tkinter as tk
import tkintermapview

class MapFrameClass:

    def buildFrame(self, fatherFrame):
        self.fatherFrame = fatherFrame
        self.MapFrame = tk.Frame(fatherFrame)

        self.map_widget = tkintermapview.TkinterMapView(self.MapFrame, width=800, height=600, corner_radius=0)
        self.map_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga",
                                        max_zoom=22)
        self.map_widget.set_position(41.275946, 1.987475)
        self.map_widget.set_zoom(20)

        self.map_widget.add_right_click_menu_command(label="Insert WP", command=self.add_marker_event,pass_coords=True)
        self.count = 0
        self.positions = []
        self.markers = []

        return self.MapFrame

    def add_marker_event(self, position):
        self.count = self.count + 1
        marker = self.map_widget.set_marker(position[0], position[1], text=self.count)

        if self.count > 1:
            path = self.map_widget.set_path([self.positions[-1], position], color='red')

        self.positions.append(position)
        self.markers.append(marker)