/**
 * Photo gallery configuration
 *
 * Sections: group photos by topic. Move photos between sections as needed.
 *
 * For each photo:
 * - dzi: path to the .dzi file
 * - thumb: path to the thumbnail
 * - title: display name
 * - description: optional caption
 * - width, height: optional — shown as dimensions; auto-fetched from DZI if omitted
 * - downloadUrl: optional — full-res download link (host original image and set this)
 * - rotation: optional — 90, 180, or 270 to fix wrong orientation
 */

window.PHOTO_SECTIONS = [
  {
    title: 'Niagara Falls',
    photos: [
      { dzi: 'images/DSC04967-Pano-3/DSC04967-Pano-3.dzi', thumb: 'images/DSC04967-Pano-3/thumb.jpg', title: 'Dsc04967 Pano 3', description: '396 MP', width: 36260, height: 10930, downloadUrl: 'original/DSC04967-Pano-3.jpg' },
      { dzi: 'images/IMG_0860-Pano/IMG_0860-Pano.dzi', thumb: 'images/IMG_0860-Pano/thumb.jpg', title: 'Img 0860 Pano', description: '115 MP', width: 30932, height: 3725, downloadUrl: 'original/IMG_0860-Pano.jpg' },
      { dzi: 'images/IMG_2921-Pano-Pano/IMG_2921-Pano-Pano.dzi', thumb: 'images/IMG_2921-Pano-Pano/thumb.jpg', title: 'Img 2921 Pano Pano', description: '54 MP', width: 16655, height: 3262, downloadUrl: 'original/IMG_2921-Pano-Pano.jpg' },
      { dzi: 'images/DSC04982-Pano/DSC04982-Pano.dzi', thumb: 'images/DSC04982-Pano/thumb.jpg', title: 'Dsc04982 Pano', description: '36 MP', width: 9279, height: 3953, downloadUrl: 'original/DSC04982-Pano.jpg' },
      { dzi: 'images/DSC_7296-Pano-Pano/DSC_7296-Pano-Pano.dzi', thumb: 'images/DSC_7296-Pano-Pano/thumb.jpg', title: 'Dsc 7296 Pano Pano', description: '20 MP', width: 8239, height: 2448, downloadUrl: 'original/DSC_7296-Pano-Pano.jpg' },
      { dzi: 'images/DSC_7296-Pano-Pano-2/DSC_7296-Pano-Pano-2.dzi', thumb: 'images/DSC_7296-Pano-Pano-2/thumb.jpg', title: 'Dsc 7296 Pano Pano 2', description: '20 MP', width: 8239, height: 2448, downloadUrl: 'original/DSC_7296-Pano-Pano-2.jpg' },
      { dzi: 'images/8-Pano-Pano/8-Pano-Pano.dzi', thumb: 'images/8-Pano-Pano/thumb.jpg', title: '8 Pano Pano', description: '41 MP', width: 18972, height: 2175, downloadUrl: 'original/8-Pano-Pano.jpg' },
      { dzi: 'images/DSC04735-Pano/DSC04735-Pano.dzi', thumb: 'images/DSC04735-Pano/thumb.jpg', title: 'Dsc04735 Pano', description: '36 MP', width: 9494, height: 3798, downloadUrl: 'original/DSC04735-Pano.jpg' },

    ]
  },
  {
    title: 'British Columbia',
    photos: [
      { dzi: 'images/IMG_3807-Pano/IMG_3807-Pano.dzi', thumb: 'images/IMG_3807-Pano/thumb.jpg', title: 'Img 3807 Pano', description: '50 MP', width: 16080, height: 3142, downloadUrl: 'original/IMG_3807-Pano.jpg' },
      { dzi: 'images/IMG_9963-Pano-Pano-Edit-2/IMG_9963-Pano-Pano-Edit-2.dzi', thumb: 'images/IMG_9963-Pano-Pano-Edit-2/thumb.jpg', title: 'Img 9963 Pano Pano Edit 2', description: '157 MP', width: 24676, height: 6401, downloadUrl: 'original/IMG_9963-Pano-Pano-Edit-2.jpg' },
      { dzi: 'images/IMG_2928-Pano/IMG_2928-Pano.dzi', thumb: 'images/IMG_2928-Pano/thumb.jpg', title: 'Img 2928 Pano', description: '98 MP', width: 28657, height: 3442, downloadUrl: 'original/IMG_2928-Pano.jpg' },
      { dzi: 'images/IMG_7176-Pano/IMG_7176-Pano.dzi', thumb: 'images/IMG_7176-Pano/thumb.jpg', title: 'Img 7176 Pano', description: '98 MP', width: 41758, height: 2348, downloadUrl: 'original/IMG_7176-Pano.jpg' },
      { dzi: 'images/IMG_9947-Pano/IMG_9947-Pano.dzi', thumb: 'images/IMG_9947-Pano/thumb.jpg', title: 'Img 9947 Pano', description: '67 MP', width: 18207, height: 3685, downloadUrl: 'original/IMG_9947-Pano.jpg' },
      { dzi: 'images/IMG_1058-Enhanced-NR-Edit/IMG_1058-Enhanced-NR-Edit.dzi', thumb: 'images/IMG_1058-Enhanced-NR-Edit/thumb.jpg', title: 'Img 1058 Enhanced Nr Edit', description: '30 MP', width: 9114, height: 3366, downloadUrl: 'original/IMG_1058-Enhanced-NR-Edit.jpg' },
      { dzi: 'images/IMG_8439-Pano-Edit/IMG_8439-Pano-Edit.dzi', thumb: 'images/IMG_8439-Pano-Edit/thumb.jpg', title: 'Img 8439 Pano Edit', description: '76 MP', width: 10711, height: 7141, downloadUrl: 'original/IMG_8439-Pano-Edit.jpg' },
      { dzi: 'images/scan0004/scan0004.dzi', thumb: 'images/scan0004/thumb.jpg', title: 'Scan0004', description: '190 MP', width: 13788, height: 13788, downloadUrl: 'original/scan0004.jpg' },
      { dzi: 'images/scan0006/scan0006.dzi', thumb: 'images/scan0006/thumb.jpg', title: 'Scan0006', description: '194 MP', width: 13941, height: 13941, downloadUrl: 'original/scan0006.jpg' },
      { dzi: 'images/scan0007/scan0007.dzi', thumb: 'images/scan0007/thumb.jpg', title: 'Scan0007', description: '191 MP', width: 13843, height: 13843, downloadUrl: 'original/scan0007.jpg' },
      { dzi: 'images/IMG_6700-Pano/IMG_6700-Pano.dzi', thumb: 'images/IMG_6700-Pano/thumb.jpg', title: 'Img 6700 Pano', description: '107 MP', width: 22508, height: 4781, downloadUrl: 'original/IMG_6700-Pano.jpg' },
      { dzi: 'images/IMG_6700-Pano-2/IMG_6700-Pano-2.dzi', thumb: 'images/IMG_6700-Pano-2/thumb.jpg', title: 'Img 6700 Pano 2', description: '86 MP', width: 22508, height: 3844, downloadUrl: 'original/IMG_6700-Pano-2.jpg' },
      { dzi: 'images/DSC_8816-Pano-Edit/DSC_8816-Pano-Edit.dzi', thumb: 'images/DSC_8816-Pano-Edit/thumb.jpg', title: 'Dsc 8816 Pano Edit', description: '60 MP', width: 24267, height: 2473, downloadUrl: 'original/DSC_8816-Pano-Edit.jpg' },

    ]
  },
  {
    title: 'China',
    photos: [
      { dzi: 'images/_MG_6771-Pano/_MG_6771-Pano.dzi', thumb: 'images/_MG_6771-Pano/thumb.jpg', title: ' Mg 6771 Pano', description: '109 MP', width: 28664, height: 3813, downloadUrl: 'original/_MG_6771-Pano.jpg' },
      { dzi: 'images/_MG_6048-Pano/_MG_6048-Pano.dzi', thumb: 'images/_MG_6048-Pano/thumb.jpg', title: ' Mg 6048 Pano', description: '65 MP', width: 17445, height: 3781, downloadUrl: 'original/_MG_6048-Pano.jpg' },
      { dzi: 'images/_MG_7636-Pano/_MG_7636-Pano.dzi', thumb: 'images/_MG_7636-Pano/thumb.jpg', title: ' Mg 7636 Pano', description: '182 MP', width: 47573, height: 3831, downloadUrl: 'original/_MG_7636-Pano.jpg' },
      { dzi: 'images/_MG_2516-Pano/_MG_2516-Pano.dzi', thumb: 'images/_MG_2516-Pano/thumb.jpg', title: ' Mg 2516 Pano', description: '36 MP', width: 12903, height: 2825, downloadUrl: 'original/_MG_2516-Pano.jpg' },
      { dzi: 'images/_MG_2528-Pano/_MG_2528-Pano.dzi', thumb: 'images/_MG_2528-Pano/thumb.jpg', title: ' Mg 2528 Pano', description: '59 MP', width: 10919, height: 5474, downloadUrl: 'original/_MG_2528-Pano.jpg' },
      { dzi: 'images/_MG_0792-Pano-Edit/_MG_0792-Pano-Edit.dzi', thumb: 'images/_MG_0792-Pano-Edit/thumb.jpg', title: ' Mg 0792 Pano Edit', description: '43 MP', width: 10806, height: 3990, downloadUrl: 'original/_MG_0792-Pano-Edit.jpg' },


    ]
  },
  {
    title: 'Enlargements',
    photos: [
      { dzi: 'images/scan0004/scan0004.dzi', thumb: 'images/scan0004/thumb.jpg', title: 'Scan0004', description: '190 MP', width: 13788, height: 13788, downloadUrl: 'original/scan0004.jpg' },
      { dzi: 'images/scan0006/scan0006.dzi', thumb: 'images/scan0006/thumb.jpg', title: 'Scan0006', description: '194 MP', width: 13941, height: 13941, downloadUrl: 'original/scan0006.jpg' },
      { dzi: 'images/scan0007/scan0007.dzi', thumb: 'images/scan0007/thumb.jpg', title: 'Scan0007', description: '191 MP', width: 13843, height: 13843, downloadUrl: 'original/scan0007.jpg' },
      { dzi: 'images/img034/img034.dzi', thumb: 'images/img034/thumb.jpg', title: 'Img034', description: '204 MP', width: 17919, height: 11434, downloadUrl: 'original/img034.jpg', rotation: 90 },
      { dzi: 'images/img063/img063.dzi', thumb: 'images/img063/thumb.jpg', title: 'Img063', description: '114 MP', width: 13408, height: 8512, downloadUrl: 'original/img063.jpg', rotation: 270 },
      { dzi: 'images/img065/img065.dzi', thumb: 'images/img065/thumb.jpg', title: 'Img065', description: '113 MP', width: 13343, height: 8512, downloadUrl: 'original/img065.jpg', rotation: 270 },
      { dzi: 'images/Capture One Catalog17508/Capture One Catalog17508.dzi', thumb: 'images/Capture One Catalog17508/thumb.jpg', title: 'Capture One Catalog17508', description: '323 MP', width: 20772, height: 15590, downloadUrl: 'original/Capture One Catalog17508.jpg' },
      { dzi: 'images/w 16/w 16.dzi', thumb: 'images/w 16/thumb.jpg', title: 'W 16', description: '85 MP', width: 10686, height: 8020, downloadUrl: 'original/w 16.jpg' },
      { dzi: 'images/_MG_0239-Enhanced-NR-Edit/_MG_0239-Enhanced-NR-Edit.dzi', thumb: 'images/_MG_0239-Enhanced-NR-Edit/thumb.jpg', title: ' Mg 0239 Enhanced Nr Edit', description: '66 MP', width: 10012, height: 6674, downloadUrl: 'original/_MG_0239-Enhanced-NR-Edit.jpg' },
      { dzi: 'images/IMG_9114-Pano/IMG_9114-Pano.dzi', thumb: 'images/IMG_9114-Pano/thumb.jpg', title: 'Img 9114 Pano', description: '33 MP', width: 11265, height: 3002, downloadUrl: 'original/IMG_9114-Pano.jpg' },
      { dzi: 'images/IMG_9145-Edit/IMG_9145-Edit.dzi', thumb: 'images/IMG_9145-Edit/thumb.jpg', title: 'Img 9145 Edit', description: '103 MP', width: 12480, height: 8320, downloadUrl: 'original/IMG_9145-Edit.jpg' },
    ]
  },
  {
    title: 'Astro',
    photos: [
      { dzi: 'images/IMG_0323_lapl6_ap1641_Drizzle30-Edit/IMG_0323_lapl6_ap1641_Drizzle30-Edit.dzi', thumb: 'images/IMG_0323_lapl6_ap1641_Drizzle30-Edit/thumb.jpg', title: 'Img 0323 Lapl6 Ap1641 Drizzle30 Edit', description: '81 MP', width: 9000, height: 9000, downloadUrl: 'original/IMG_0323_lapl6_ap1641_Drizzle30-Edit.jpg' },
      { dzi: 'images/Autosave-2/Autosave-2.dzi', thumb: 'images/Autosave-2/thumb.jpg', title: 'Autosave 2', description: '82 MP', width: 11086, height: 7405, downloadUrl: 'original/Autosave-2.jpg' },
      { dzi: 'images/IMG_0352_lapl3_ap4112-Edit-2/IMG_0352_lapl3_ap4112-Edit-2.dzi', thumb: 'images/IMG_0352_lapl3_ap4112-Edit-2/thumb.jpg', title: 'Img 0352 Lapl3 Ap4112 Edit 2', description: '95 MP', width: 9760, height: 9760, downloadUrl: 'original/IMG_0352_lapl3_ap4112-Edit-2.jpg' },
    ]
  },
  {
    title: 'Other',
    photos: [
      { dzi: 'images/DSC03179-Pano/DSC03179-Pano.dzi', thumb: 'images/DSC03179-Pano/thumb.jpg', title: 'Dsc03179 Pano', description: '62 MP', width: 21155, height: 2941, downloadUrl: 'original/DSC03179-Pano.jpg' },
      { dzi: 'images/IMG_8955/IMG_8955.dzi', thumb: 'images/IMG_8955/thumb.jpg', title: 'Img 8955', description: '79 MP', width: 10944, height: 7296, downloadUrl: 'original/IMG_8955.jpg' },
    ]
  }
];
