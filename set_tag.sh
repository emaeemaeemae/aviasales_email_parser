LATEST_TAG=$(docker images --filter=reference="aviasales" --format "{{.Tag}}" | sort -rV | grep 0 | head -n 1)
if [[ -z "$LATEST_TAG" ]] || [[ "$LATEST_TAG" == "latest" ]]; then
  LATEST_TAG="0.1"
elif [[ -n "$LATEST_TAG" ]]; then
  PREV_TAG=$LATEST_TAG
  LATEST_TAG=$(echo $LATEST_TAG | awk -F"." '{i=$2;i+=1} END {print $1"."i}')
fi