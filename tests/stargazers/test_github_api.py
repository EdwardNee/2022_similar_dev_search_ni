from collections import Counter

import pytest

from repo_processing.stargazers.github_api import process_stargazers

result_counter = Counter({"ADKosm/lsml-2022-public": 1,
                          "Apress/practical-tla-plus": 1,
                          "BishopFox/unredacter": 1,
                          "Bo0oM/fuzz.txt": 1,
                          "Checkmarx/kics": 1,
                          "Genymobile/scrcpy": 1,
                          "IgorSamohin/mental-care-by-marusia": 1,
                          "IntelRealSense/librealsense": 1,
                          "Iteo/AndroidCleanUITests": 1,
                          "KEKDATA/KEKPETS": 1,
                          "KathanP19/JSFScan.sh": 1,
                          "LonamiWebs/Telethon": 1,
                          "Nate711/StanfordDoggoProject": 1,
                          "OpenFeign/feign": 1,
                          "OpenFlutter/flutter_screenutil": 1,
                          "Sloy/android-dependency-injection-performance": 1,
                          "TonyBlock/homework-4": 1,
                          "VKCOM/VKUI": 1,
                          "VKCOM/vk-bridge": 1,
                          "VKCOM/vk-miniapps-deploy": 1,
                          "Whiletruedoend/Vk-to-telegram-transfer-bot": 1,
                          "Widdershin/flask-desktop": 1,
                          "Xyl2k/TSA-Travel-Sentry-master-keys": 1,
                          "adaptyteam/AdaptySDK-Android": 1,
                          "aioverlords/Google-Cloud-Platform-Killswitch": 1,
                          "aislandener/flutter_social_share": 1,
                          "android/architecture-samples": 1,
                          "android/location-samples": 1,
                          "androidx/androidx": 1,
                          "avelino/awesome-go": 1,
                          "ayles/heart": 1,
                          "buildship-dev/nft-contracts": 1,
                          "buildship-dev/webflow-nft-components": 1,
                          "c0defather/Khameleon": 1,
                          "callstack/linaria": 1,
                          "ciandt-mobile/android-recyclerview-binding": 1,
                          "codecrafters-io/build-your-own-x": 1,
                          "cookiecutter-flask/cookiecutter-flask": 1,
                          "corona10/goimagehash": 1,
                          "csvitlik/static_analysis_tools": 1,
                          "danlkv/tgflow": 1,
                          "darwin-morocho/flutter-facebook-auth": 1,
                          "dlutton/flutter_tts": 1,
                          "dnfield/flutter_svg": 1,
                          "evvvsss/fractol": 1,
                          "facebook/flux": 1,
                          "felangel/bloc": 1,
                          "felixhao28/JSCPP": 1,
                          "flipperdevices/Flipper-Android-App": 1,
                          "flipperdevices/flipper-hackathon-moscow": 1,
                          "flutterchina/dio": 1,
                          "freetonsurfer/ton_client_flutter": 1,
                          "frontend-park-mail-ru/2021_2_LadnoDavayteBezRoflov":
                              1,
                          "frontend-park-mail-ru/2022_1_SamoeKrNaz": 1,
                          "futurice/android-best-practices": 1,
                          "go-park-mail-ru/2021_2_LadnoDavayteBezRoflov": 1,
                          "go-park-mail-ru/2022_1_SamoeKrNaz": 1,
                          "gojp/goreportcard": 1,
                          "golang/go": 1,
                          "google/flexbox-layout": 1,
                          "hse-system-design-2021/public": 1,
                          "hukenovs/dsp-theory": 1,
                          "ibulgakovzzx/marvel-characters": 1,
                          "internetwache/GitTools": 1,
                          "jamesblasco/modal_bottom_sheet": 1,
                          "jangrewe/gitlab-ci-android": 1,
                          "kotlin-telegram-bot/kotlin-telegram-bot": 1,
                          "leralerale/CourseProject_2nd_Year": 1,
                          "leshiy1295/technopark_c_c_plus_plus": 1,
                          "let-robots-reign/OGE_ENG_WEB": 1,
                          "let-robots-reign/react-lessons": 1,
                          "letsar/flutter_slidable": 1,
                          "limitedeternity/foxford_courses": 1,
                          "loomnetwork/cryptozombies-lesson-code": 1,
                          "lucas-clemente/quic-go": 1,
                          "luizgrp/SectionedRecyclerViewAdapter": 1,
                          "mailcourses/python_backend_autumn_2021": 1,
                          "matter-labs/awesome-zero-knowledge-proofs": 1,
                          "mkrl/misbrands": 1,
                          "mobile-roadmap/android-developer-roadmap": 1,
                          "mtrempoltsev/tarantool_highload": 1,
                          "negezor/vk-io": 1,
                          "ngallazzi/cleanarchitectureblueprints": 1,
                          "nosequeldeebee/blockchain-tutorial": 1,
                          "ntnhon/RecyclerViewRowOptionsDemo": 1,
                          "onebone/compose-collapsing-toolbar": 1,
                          "ossu/computer-science": 1,
                          "pichenettes/eurorack": 1,
                          "polis-vk/2022-android": 1,
                          "pszklarska/FlutterPubVersionChecker": 1,
                          "raspberrypi/linux": 1,
                          "rust-unofficial/awesome-rust": 1,
                          "sanogueralorenzo/Android-Kotlin-Clean-Architecture":
                              1,
                          "sberoch/RickAndMorty-AndroidArchitectureSample":
                              1,
                          "sirius-ai/MobileFaceNet_TF": 1,
                          "storm-devs/storm-engine": 1,
                          "tarantool/cartridge-cli": 1,
                          "tarantool/sysprog": 1,
                          "teh-cmc/go-internals": 1,
                          "telegraf/telegraf": 1,
                          "tiangolo/fastapi": 1,
                          "valiotti/leftjoin": 1,
                          "velmurugan-murugesan/Android-Example": 1,
                          "venom26/recon": 1,
                          "vganin/dpad-aware-recycler-view": 1,
                          "vk-education/VoluptuousWaffles": 1,
                          "vk-education/android-samples": 8,
                          "vlang/v": 1,
                          "vmadalin/android-modular-architecture": 1,
                          "walaura/emoji-avatars": 1,
                          "wavedrom/wavedrom.github.io": 1,
                          "whitelext/dota_hunter": 1,
                          "zawadz88/NavigationComponentPlayground": 1})


@pytest.mark.parametrize("url, expected_counter",
                         [("vk-education/android-samples", result_counter)])
def test_stargazers_returns_right_counter(url: str,
                                          expected_counter: Counter,
                                          key: str) -> None:
    """
    Tests process_stargazers function is returning Counter type and that
    returns right data for testing repository
    example with different urls.

    :param url: URL to repository.
    :param expected_counter: Expected result.
    :param key: GitHub API key.
    """

    parse = process_stargazers(github_token=key, current_repo_name=url)

    assert (type(parse) is Counter) and (parse == expected_counter) and (
            len(parse) == len(expected_counter))
