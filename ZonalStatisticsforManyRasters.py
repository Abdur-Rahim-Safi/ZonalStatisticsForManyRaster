root = QgsProject.instance().layerTreeRoot()
for layer in root.children():
    #print(layer.name())
    if layer.name().startswith('L3_GEZ_BF'):
        prefix = layer.name()[-4:]
        #print(prefix)
        params = { 'COLUMN_PREFIX' : prefix+'_', 'INPUT_VECTOR' : 'bfdatafixedgeodataselectedfieldsfortest', 'INPUT_RASTER' : layer.name(), 'RASTER_BAND' : 1, 'STATISTICS' : [2] }
        processing.run("qgis:zonalstatistics", params)