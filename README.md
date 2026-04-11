# txt_2_tif_dem_builder v1.1.0

G空間情報センター等でダウンロードできるtxt/csv形式のDEMを、GeoTIFF形式に変換するQGISプラグインです。  
This plugin converts DEM data in txt/csv format (e.g., from the Geospatial Information Center) to GeoTIFF.

![](./docs/demo.gif)

## 使い方 / Usage

1. プラグインをインストールすると、以下のアイコンがツールバーに表示されます。クリックするとツールが起動します。  
   After installing the plugin, the following icon will appear in the toolbar. Click it to launch the tool.

<img src="./icon.png" alt="icon" width="100">

2. 以下のパラメータを設定します。  
   Set the following parameters:

- **入力データ / Input Data**
  - 単一のtxt/csvファイル  
    Single txt/csv file  
  - または 複数ファイルを含むフォルダ  
    Or a folder containing multiple files  

- **列設定 / Column Settings**
  - X, Y, Z 座標列  
    X, Y, Z coordinate columns  
  - 区切り文字  
    Delimiter  
  - スキップ行数（ヘッダーなど）  
    Number of rows to skip (e.g., header rows)  

- **出力設定 / Output Settings**
  - 出力座標系  
    Output CRS  
  - 単一ファイル入力時：出力ファイル名を指定  
    For single file input: specify output file name  
  - フォルダ入力時：  
    For folder input:  
    - 「個別tifを出力」  
      Output individual TIFFs  
    - 「マージtifを出力」  
      Output Merged TIFF  
    を選択し、それぞれ出力先を指定  
    Select the desired options and specify output destinations  

3. 「実行」をクリック  
   Click "Run"

<img src="./docs/UI.png" alt="UI" width="800">

## 留意事項 / Notes

- 入力点の座標は、出力ラスタセルの**中心**に対応するよう処理されます。  
  Input point coordinates are treated as the **center** of output raster cells.  

- NoData値は `-9999` が割り当てられます。  
  The NoData value is set to `-9999`.  

- 入力ファイルの形式（区切り文字・列構成）に応じて、適切にパラメータを設定してください。  
  Please set parameters according to the input file format (delimiter, column structure, etc.).  

## Author

Mizuki TAKIGAWA