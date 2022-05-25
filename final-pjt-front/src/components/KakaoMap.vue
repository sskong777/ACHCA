<template>
  <v-container>
    <v-row>
      <v-col> </v-col>
    </v-row>
    <v-row justify="center">
      <v-col cols="10">
        <v-sheet
          col="9"
          min-height="20vh"
          rounded="lg"
          class="col justify-content-center align-items-center"
        >
          <v-col cols="12" col="6">
            <v-text-field
              v-model="keyWord"
              @keyup.enter="keyWordSearch"
              label="Theater"
              placeholder="지역을 입력해주세요!"
              filled
              solo
              hide-details="auto"
              color="purple"
              loading
            ></v-text-field>
          </v-col>
          <!-- <input :v-model="keyWord" @keyup.enter="keyWordSearch" type="text" id="keyword" v-model="keyWord"> -->
          <v-btn id="btn" @click="keyWordSearch">SEARCH</v-btn>
          <!-- <v-chip class="ma-2" color="primary" label><v-icon left>mdi-account-circle-outline</v-icon>{{ currentUser.username }}</v-chip> -->
        </v-sheet>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col cols="10">
        <v-sheet min-height="70vh" rounded="lg">
          <div id="map" style="height: 70vh"></div>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  data: () => ({
    keyWord: "",
    local: [],
  }),
  mounted() {
    if (window.kakao && window.kakao.maps) {
      this.initMap();
    } else {
      const script = document.createElement("script");
      /* global kakao */
      script.onload = () => kakao.maps.load(this.initMap);
      script.src =
        "//dapi.kakao.com/v2/maps/sdk.js?appkey=b4c4152d46aff7b528f8e55917a9a7d5&autoload=false&libraries=services";
      document.head.appendChild(script);
    }
  },
  computed: {
    ...mapGetters(["currentUser"]),
  },
  methods: {
    ...mapActions(["fetchCurrentUser"]),
    // 현재 위치
    initMap() {
      var container = document.getElementById("map");
      var options = {
        center: new kakao.maps.LatLng(36.107173983233736, 128.41619087327746),
        level: 6,
      };
      var map = new kakao.maps.Map(container, options);
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {
          const lat = position.coords.latitude;
          const lon = position.coords.longitude;

          const locPosition = new kakao.maps.LatLng(lat, lon);
          const message = "사용자 현재 위치";

          displayMarker(locPosition, message);
        });
      } else {
        var locPosition = new kakao.maps.LatLng(
          36.107173983233736,
          128.41619087327746
        );
        var message = "현재 위치를 찾을 수 없습니다";

        displayMarker(locPosition, message);
      }
      function displayMarker(locPosition, message) {
        const marker = new kakao.maps.Marker({
          map: map,
          position: locPosition,
        });

        const iwContent = message;
        const iwRemovaable = true;

        var infowindow = new kakao.maps.InfoWindow({
          content: iwContent,
          removavle: iwRemovaable,
        });
        infowindow.open(map, marker);

        map.setCenter(locPosition);
      }
    },

    addScript() {
      const script = document.createElement("script");
      script.onload = () => kakao.maps.load(this.initMap);
      script.src =
        "//dapi.kakao.com/v2/maps/sdk.js?appkey=b4c4152d46aff7b528f8e55917a9a7d5&autoload=false&libraries=services";
      document.head.appendChild(script);
    },

    keyWordSearch() {
      var infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });

      const mapContainer = document.getElementById("map");
      const options = {
        center: new kakao.maps.LatLng(36.107173983233736, 128.41619087327746),
        level: 4,
      };

      const map = new kakao.maps.Map(mapContainer, options);

      const ps = new kakao.maps.services.Places();
      ps.keywordSearch(this.keyWord + " 영화관", placesSearchCB, {
        radius: 5000,
      });

      function placesSearchCB(data, status) {
        if (status === kakao.maps.services.Status.OK) {
          const bounds = new kakao.maps.LatLngBounds();

          for (var i = 0; i < data.length; i++) {
            displayMarker(data[i]);
            bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
          }
          map.setBounds(bounds);
        } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
          console.log("hi");
          alert("검색 결과가 없습니다");
        } else if (status === kakao.maps.services.Status.ERROR) {
          alert("검색 결과 중 오류가 발생했습니다");
        }

        function displayMarker(place) {
          var marker = new kakao.maps.Marker({
            map: map,
            position: new kakao.maps.LatLng(place.y, place.x),
          });

          kakao.maps.event.addListener(marker, "click", function () {
            infowindow.setContent(
              '<div style="padding:5px;font-size:0.8rem;">' +
                place.place_name +
                "</div>"
            );
            infowindow.open(map, marker);
          });
        }
      }
    },
    // keyWordSearch () {
    //   var markers = []

    //   var mapContainer = document.getElementById('map')
    //   var mapOption = {
    //     center: new kakao.maps.LatLng(37.566826, 126.9786867),
    //     level: 3
    //   }

    //   var map = new kakao.maps.Map(mapContainer, mapOption)

    //   var ps = new kakao.maps.services.Places()

    //   var infowindow = new kakao.maps.InfoWindow({ zIndex: 1})

    //   searchPlaces()

    //   function searchPlaces() {
    //     var keyword = '영화관'

    //     if (!keyword.replace(/^\s+|\s+$/g, '')) {
    //       alert('키워드를 입력하세요')
    //       return false
    //     }

    //     ps.keywordSearch(keyword, placesSearchCB)
    //   }

    //   function placesSearchCB (data, status, pagination) {
    //     if (status === kakao.maps.services.Status.OK) {
    //       displayPlaces(data)

    //       displayPagination(pagination)
    //     } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
    //       alert('검색 결과가 없습니다')
    //     } else if (status === kakao.maps.services.Status.ERROR) {
    //       alert('거맥 결과 중 오류가 발생했습니다')
    //     }
    //   }

    //   function displayPlaces (places) {
    //     var fragment = document.createDocumentFragment()
    //     var bounds = new kakao.maps.LatLngBounds()

    //     removeMarker()

    //     for (var i=0; i< places.length; i++) {
    //       var placePosition = new kakao.maps.LatLng(places[i].y, places[i].x)
    //       var marker = addMarker(placePosition, i)
    //       var itemEl = getListItem(i, places[i])

    //       bounds.extend(placePosition);

    //       (function (marker, title) {
    //         kakao.maps.event.addListener(marker, 'mouseover', function () {
    //           displayInfowindow(marker, title)
    //         })

    //         kakao.maps.event.addListener(marker, 'mouseout', function() {
    //           infowindow.close()
    //         })

    //         itemEl.onmouseover = function () {
    //           displayInfowindow(marker, title)
    //         }

    //         itemEl.onmouseout = function () {
    //           infowindow.close()
    //         }
    //       })(marker, places[i].place_name)

    //       fragment.appendChild(itemEl)
    //     }

    //     map.setBounds(bounds)
    //   }

    //   function getListItem (index, places) {
    //     var el = document.createElement('li')
    //     var itemStr = '<span class="markerbg marker_' + (index + 1) + '"></span>' +
    //           '<div class="info">' + '    <h5>'+places.place_name +'</h5>'
    //     if (places.road_address_name) {
    //       itemStr += '      <span>'+places.road_address_name +'</span>' + '      <span class="jibun gray">' + places.address_name + '</span>'
    //     } else {
    //       itemStr += '      <span>'+ places.address_name + '</span>'
    //     }

    //     itemStr += '    <span class="tel">' + places.phone + '</span>' + '</div>'

    //     el.innerHTML = itemStr
    //     el.className = 'item'

    //     return el
    //   }

    //   function addMarker(position, idx) {
    //     var imageSrc = 'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_red.png'
    //     var imageSize = new kakao.maps.Size(36, 37)
    //     var imgOptions = {
    //       spriteSize: new kakao.maps.Size(64, 69),
    //       spriteOrigin: new kakao.maps.Point(27, (idx * 46) + 10),
    //       offset: new kakao.maps.Point(13, 37)
    //     }
    //     var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imgOptions)
    //     var marker = new kakao.maps.Marker({
    //       position: position,
    //       image: markerImage
    //     })

    //     marker.setMap(map)
    //     markers.push(marker)

    //     return marker
    //   }

    //   function removeMarker() {
    //     for (var i=0; i< markers.length; i++) {
    //       markers[i].setMap(null)
    //     }
    //     markers = []
    //   }

    //   function displayPagination(pagination) {

    //     var fragment = document.createDocumentFragment()
    //     var i

    //     for (i = 1; i<= pagination.last; i++) {
    //       var el = document.createElement('a')
    //       el.href = '#'
    //       el.innerHTML = i

    //       if (i === pagination.current) {
    //         el.className = 'on'
    //       } else {
    //         el.onclick = (function (i) {
    //           return function () {
    //             pagination.gotoPage(i)
    //           }
    //         })(i)
    //       }
    //       fragment.appendChild(el)
    //     }
    //   }

    //   function displayInfowindow(marker, title) {
    //     var content = '<div style="padding:5px;z-index:1;">' + title + '</div>'

    //     infowindow.setContent(content)
    //     infowindow.open(map, marker)
    //   }

    // }
  },
};
</script>

<style>
#btn {
  background-color: mediumslateblue;
  color: white;
}
</style>
