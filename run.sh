echo "Start update"
. ./set_tag.sh
export LATEST_TAG
export PREV_TAG

docker image rm -f aviasales:"${PREV_TAG}"
docker rm --force aviasales
docker build -t aviasales:"${LATEST_TAG}" .
docker run --name aviasales -d --restart=always aviasales:"${LATEST_TAG}"
echo "Done"
