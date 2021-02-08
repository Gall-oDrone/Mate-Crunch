import React from "react";
import "../assets/purchasePageAndFooter.css";
import * as THREE from 'three';
import jsonf from "../svg-to-coordinates-master-Globe/points.json";
const globeRadius = 100;
const globeWidth = 4098 / 2;
const globeHeight = 1968 / 2;
class SphereCont extends React.PureComponent {
      
        convertFlatCoordsToSphereCoords(x, y) {
          let latitude = ((x - globeWidth) / globeWidth) * -180;
          let longitude = ((y - globeHeight) / globeHeight) * -90;
          latitude = (latitude * Math.PI) / 180;
          longitude = (longitude * Math.PI) / 180;
          const radius = Math.cos(longitude) * globeRadius;
      
          return {
            x: Math.cos(latitude) * radius,
            y: Math.sin(longitude) * globeRadius,
            z: Math.sin(latitude) * radius
          };
        }
  
        componentDidMount() {
            var scene = new THREE.Scene();
            var camera = new THREE.PerspectiveCamera( 75, 480/450, 0.1, 1000 );
            camera.position.set(0,0,250);
            var renderer = new THREE.WebGLRenderer();
            renderer.setSize( 480, 450 );
            this.mount.appendChild( renderer.domElement );
            var light = new THREE.HemisphereLight(0xffffbb, 0x080820, 1);
            scene.add(light);

            const points = jsonf.points
            const vertices = []
            for (let point of points) {
                let width = 180 
                let height = 150
                const { x, y, z } = this.convertFlatCoordsToSphereCoords(
                    point.x,
                    point.y,
                    width,
                    height
                );
        
                vertices.push(x, y, z)
            }
            const positions = new Float32Array( vertices );
            // length: 117486
            console.log("culo:", positions) 
            const mergedGeometry = new THREE.BufferGeometry();
            mergedGeometry.setAttribute( 'position', new THREE.BufferAttribute( positions, 3 ) );

            const material = new THREE.MeshStandardMaterial( {color: "#FFFF00",  wireframe: true});

            var geometory = new THREE.SphereGeometry(0.5,1,1);
            var material2 = new THREE.MeshBasicMaterial({
              color: 0x1a1a1a
            });
            var mesh = new THREE.Mesh(geometory, material2);

            const particles = new THREE.Points( mergedGeometry, material );
            scene.add( particles );
            
            var animate = function () {
                particles.rotation.x = 0.00
                particles.rotation.y = 0.01
                particles.rotation.z = 0.00
                requestAnimationFrame( animate );
                renderer.render( scene, camera );
                camera.lookAt(scene.position);
            };
            animate();
        }
      
   render() {
        return (
            <div ref={ref => (this.mount = ref)} />
        );
    }
}

export default (SphereCont);