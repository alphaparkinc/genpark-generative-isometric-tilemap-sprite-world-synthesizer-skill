from client import GenerativeIsometricTilemapSpriteWorldSynthesizerClient

def main():
    client = GenerativeIsometricTilemapSpriteWorldSynthesizerClient()
    res = client.synthesize_tilemap_world_pack('Cyberpunk Neo-Tokyo Rooftop Slums with neon cables and solar arrays', 64)
    print('World Pack ID: ' + res['world_pack_id'] + ' | Theme: ' + res['theme'])
    print('Resolution: ' + str(res['grid_resolution_px']) + 'x' + str(res['grid_resolution_px']) + ' | Tiles: ' + str(res['unique_tiles_generated_count']))
    print('Seamless Edge Matching: ' + str(res['seamless_edge_matching_verified']) + ' | Collision Masks: ' + str(res['physics_collision_polygons_included']))
    print('SpriteSheet URL: ' + res['spritesheet_png_url'])
    print('Tiled TMX URL: ' + res['tiled_tmx_map_url'])

if __name__ == '__main__':
    main()
